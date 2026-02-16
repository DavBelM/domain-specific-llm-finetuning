"""
Medical LLM Assistant - Standalone Gradio Application

This is a standalone version of the Gradio interface that can be run locally
after fine-tuning the model using the Colab notebook.

Usage:
    python demo/gradio_app.py

Requirements:
    - Fine-tuned model checkpoint in models/ directory
    - All dependencies from requirements.txt installed
    - CUDA-compatible GPU (recommended but not required)
"""

import os
import torch
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Configuration
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
FINETUNED_MODEL_PATH = "./models/experiment_1"  # Update with your best model path

# Check if model exists
if not os.path.exists(FINETUNED_MODEL_PATH):
    print(f"Error: Fine-tuned model not found at {FINETUNED_MODEL_PATH}")
    print("Please run the Colab notebook first to train the model.")
    exit(1)

print("Loading models...")

# Configure 4-bit quantization
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)

# Load fine-tuned model
finetuned_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)
finetuned_model = PeftModel.from_pretrained(finetuned_model, FINETUNED_MODEL_PATH)

print("Models loaded successfully!")


def generate_response(model, tokenizer, question, temperature=0.7, max_tokens=150):
    """
    Generate response from model.
    
    Args:
        model: The model to use for generation
        tokenizer: The tokenizer
        question: User's medical question
        temperature: Generation temperature
        max_tokens: Maximum tokens to generate
    
    Returns:
        Generated response text
    """
    prompt = f"""<|system|>
You are a medical assistant. Answer the following medical question accurately and concisely.</s>
<|user|>
{question}</s>
<|assistant|>
"""
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=int(max_tokens),
            do_sample=True,
            temperature=temperature,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the assistant's response
    if "<|assistant|>" in response:
        response = response.split("<|assistant|>")[-1].strip()
    
    return response


def chatbot_interface(question, model_choice, temperature, max_tokens):
    """
    Gradio interface function.
    
    Args:
        question: User's medical question
        model_choice: 'Baseline' or 'Fine-tuned'
        temperature: Generation temperature
        max_tokens: Maximum tokens to generate
    
    Returns:
        Generated response
    """
    if not question.strip():
        return "Please enter a question."
    
    model = finetuned_model if model_choice == "Fine-tuned" else base_model
    
    try:
        response = generate_response(model, tokenizer, question, temperature, max_tokens)
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"


def compare_models(question, temperature, max_tokens):
    """
    Compare baseline and fine-tuned models side-by-side.
    
    Args:
        question: User's medical question
        temperature: Generation temperature
        max_tokens: Maximum tokens to generate
    
    Returns:
        Tuple of (baseline_response, finetuned_response)
    """
    if not question.strip():
        return "Please enter a question.", "Please enter a question."
    
    try:
        baseline_response = generate_response(base_model, tokenizer, question, temperature, max_tokens)
        finetuned_response = generate_response(finetuned_model, tokenizer, question, temperature, max_tokens)
        return baseline_response, finetuned_response
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return error_msg, error_msg


# Create Gradio interface
with gr.Blocks(title="Medical QA Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🏥 Medical QA Assistant
        
        Ask medical questions and get answers from our fine-tuned medical LLM assistant.
        Compare responses between the baseline and fine-tuned models.
        
        **⚠️ Disclaimer:** This is an educational project. Do NOT use for actual medical advice.
        Always consult qualified healthcare professionals for medical concerns.
        """
    )
    
    with gr.Tab("Single Model"):
        with gr.Row():
            with gr.Column():
                question_input = gr.Textbox(
                    label="Medical Question",
                    placeholder="E.g., What are the symptoms of diabetes?",
                    lines=3
                )
                
                model_choice = gr.Radio(
                    choices=["Baseline", "Fine-tuned"],
                    value="Fine-tuned",
                    label="Model Selection"
                )
                
                with gr.Row():
                    temperature = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=0.7,
                        step=0.1,
                        label="Temperature"
                    )
                    
                    max_tokens = gr.Slider(
                        minimum=50,
                        maximum=300,
                        value=150,
                        step=10,
                        label="Max Tokens"
                    )
                
                submit_btn = gr.Button("Get Answer", variant="primary")
            
            with gr.Column():
                output = gr.Textbox(
                    label="Response",
                    lines=10,
                    interactive=False
                )
        
        submit_btn.click(
            fn=chatbot_interface,
            inputs=[question_input, model_choice, temperature, max_tokens],
            outputs=output
        )
    
    with gr.Tab("Compare Models"):
        gr.Markdown("### Side-by-side comparison of Baseline vs Fine-tuned models")
        
        with gr.Row():
            compare_question = gr.Textbox(
                label="Medical Question",
                placeholder="E.g., What is hypertension?",
                lines=3
            )
        
        with gr.Row():
            compare_temp = gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="Temperature"
            )
            
            compare_tokens = gr.Slider(
                minimum=50,
                maximum=300,
                value=150,
                step=10,
                label="Max Tokens"
            )
        
        compare_btn = gr.Button("Compare Models", variant="primary")
        
        with gr.Row():
            baseline_output = gr.Textbox(
                label="Baseline Model Response",
                lines=10,
                interactive=False
            )
            
            finetuned_output = gr.Textbox(
                label="Fine-tuned Model Response",
                lines=10,
                interactive=False
            )
        
        compare_btn.click(
            fn=compare_models,
            inputs=[compare_question, compare_temp, compare_tokens],
            outputs=[baseline_output, finetuned_output]
        )
    
    # Example questions
    gr.Examples(
        examples=[
            ["What is hypertension?"],
            ["What are the symptoms of Type 2 diabetes?"],
            ["How is pneumonia diagnosed?"],
            ["What causes asthma?"],
            ["What is the treatment for anemia?"],
            ["What is the difference between type 1 and type 2 diabetes?"],
            ["What are the risk factors for heart disease?"]
        ],
        inputs=question_input
    )
    
    gr.Markdown(
        """
        ---
        ### Model Information
        
        - **Base Model:** TinyLlama-1.1B-Chat-v1.0
        - **Dataset:** Medical Flashcards (medalpaca/medical_meadow_medical_flashcards)
        - **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
        - **Training:** ~2,500 medical Q&A pairs
        
        ### About This Project
        
        This medical QA assistant was created by fine-tuning TinyLlama using LoRA on medical flashcards.
        The fine-tuned model demonstrates improved understanding of medical terminology and concepts
        compared to the baseline model.
        
        **Project Repository:** [GitHub Link]
        """
    )


if __name__ == "__main__":
    print("\n" + "="*80)
    print("Starting Medical QA Assistant")
    print("="*80)
    print(f"\nBase Model: {MODEL_NAME}")
    print(f"Fine-tuned Model: {FINETUNED_MODEL_PATH}")
    print(f"Device: {next(base_model.parameters()).device}")
    print("\nLaunching Gradio interface...")
    print("="*80 + "\n")
    
    # Launch the app
    demo.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7860,        # Default Gradio port
        share=False,             # Set to True to create public link
        debug=True
    )
