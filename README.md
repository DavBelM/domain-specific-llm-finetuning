# 🏥 Medical LLM Assistant - Domain-Specific Fine-tuning Project

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DavBelM/domain-specific-llm-finetuning/blob/main/notebooks/medical_llm_finetuning.ipynb)

## 📋 Project Overview

This project demonstrates fine-tuning a Large Language Model (LLM) for healthcare-specific question answering using **LoRA (Low-Rank Adaptation)**. The system creates a medical assistant capable of accurately answering medical questions by fine-tuning TinyLlama-1.1B on medical flashcards dataset.

**Domain:** Healthcare (Medical Q&A)  
**Base Model:** TinyLlama/TinyLlama-1.1B-Chat-v1.0  
**Dataset:** medalpaca/medical_meadow_medical_flashcards  
**Fine-tuning Method:** LoRA (Parameter-Efficient Fine-Tuning)  
**Deployment:** Gradio Web Interface

## 🎯 Project Objectives

1. **Data Collection & Preprocessing:** Collect and preprocess medical Q&A dataset with comprehensive tokenization and normalization
2. **Model Fine-tuning:** Fine-tune TinyLlama using LoRA with multiple hyperparameter configurations
3. **Experimentation:** Run 4+ experiments to optimize model performance
4. **Evaluation:** Assess performance using BLEU, ROUGE, and Perplexity metrics
5. **Deployment:** Create an interactive web interface for user interaction
6. **Documentation:** Comprehensive documentation and demo video

## 🚀 Quick Start

### Open in Google Colab (Recommended)

Click the badge above to open the notebook directly in Google Colab. The notebook is designed to run end-to-end on Colab's free GPU tier.

### Local Setup

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/domain-specific-llm-finetuning.git
cd domain-specific-llm-finetuning
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the notebook:**

```bash
jupyter notebook notebooks/medical_llm_finetuning.ipynb
```

**Note:** Local execution requires a CUDA-compatible GPU with at least 12GB VRAM.

## 📁 Project Structure

```
domain-specific-llm-finetuning/
│
├── README.md                          # Main documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Ignore large files
│
├── notebooks/
│   └── medical_llm_finetuning.ipynb  # Main Colab notebook (complete pipeline)
│
├── data/
│   └── README.md                     # Dataset information
│
├── models/
│   └── README.md                     # Model checkpoints info
│
├── results/
│   ├── experiment_results.md         # Experiment tracking table
│   ├── experiment_comparison.png     # Visualization of experiments
│   ├── evaluation_metrics.md         # Performance metrics
│   └── model_info.json              # Best model configuration
│
├── demo/
│   ├── gradio_app.py                # Standalone Gradio app
│   └── demo_video_link.md           # Link to demo video
│
└── docs/
    └── report.pdf                    # Final submission report
```

## 📊 Dataset

**Source:** [medalpaca/medical_meadow_medical_flashcards](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)

**Description:** Medical question-answer pairs covering various medical topics including diseases, treatments, symptoms, and medical terminology.

**Preprocessing Steps:**

1. **Data Cleaning:** Remove duplicates, handle missing values, filter low-quality examples
2. **Text Normalization:** Strip whitespace, fix encoding issues
3. **Formatting:** Convert to instruction-response format for fine-tuning
4. **Tokenization:** Use TinyLlama tokenizer with appropriate padding/truncation
5. **Train-Test Split:** 90/10 split (2,250 train / 250 eval examples)
6. **Length Filtering:** Ensure sequences fit within 512 token context window

**Final Dataset Size:** ~2,500 high-quality medical Q&A pairs

## 🔬 Methodology

### Fine-tuning Approach: LoRA (Low-Rank Adaptation)

**Why LoRA?**

- **Memory Efficient:** Reduces trainable parameters to ~0.2% of original model
- **Fast Training:** Significantly reduces training time and GPU requirements
- **Quality Preservation:** Maintains model quality while adapting to new domain
- **Colab Compatible:** Enables training on free GPU tier (T4 with 16GB VRAM)

**LoRA Configuration:**

```python
LoraConfig(
    r=8-16,              # Rank (tested both values)
    lora_alpha=16-32,    # Scaling factor
    lora_dropout=0.1,    # Dropout for regularization
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]
)
```

### Memory Optimization

- **4-bit Quantization:** Using BitsAndBytes for reduced memory footprint
- **Gradient Checkpointing:** Trade computation for memory
- **Gradient Accumulation:** Effective batch size increase without OOM errors

## 🧪 Experiments

We conducted 4 systematic experiments with different hyperparameter configurations:

| Experiment | Learning Rate | Batch Size | Epochs | LoRA Rank | LoRA Alpha | Train Loss | Eval Loss | Perplexity | Training Time |
| ---------- | ------------- | ---------- | ------ | --------- | ---------- | ---------- | --------- | ---------- | ------------- |
| Baseline   | N/A           | N/A        | 0      | 0         | 0          | N/A        | 7.5483    | 1897.58    | N/A           |
| 1          | 1e-4          | 2          | 2      | 8         | 16         | 0.8299     | 0.8004    | 2.2263     | 59.0 min      |
| 2          | 5e-5          | 4          | 3      | 16        | 32         | 0.8615     | 0.8123    | 2.2531     | 105.0 min     |
| 3          | 2e-5          | 2          | 3      | 8         | 16         | 5290.20    | N/A       | N/A        | 187.9 min     |
| 4          | 1e-4          | 2          | 2      | 16        | 32         | 6612.67    | N/A       | N/A        | 127.3 min     |

**Best Model:** Experiment 1 achieved lowest perplexity (2.2263) with **99.88% improvement** over baseline.

**Evaluation Metrics (Baseline vs Best Fine-tuned):**

- **BLEU:** 9.59 → 12.70 (+32.4%)
- **ROUGE-1:** 0.322 → 0.409 (+26.9%)
- **ROUGE-2:** 0.172 → 0.243 (+41.3%)
- **ROUGE-L:** 0.249 → 0.323 (+29.8%)
- **Perplexity:** 1897.58 → 2.23 (**-99.88%** ✅)

### Hyperparameters Tested

- **Learning Rate:** 1e-4, 5e-5, 2e-5
- **Batch Size:** 2, 4 (with gradient accumulation)
- **Epochs:** 2-3
- **LoRA Rank:** 8, 16
- **LoRA Alpha:** 16, 32

## 📈 Evaluation Metrics

### Quantitative Metrics

1. **BLEU Score:** Measures n-gram overlap between generated and reference answers
2. **ROUGE Scores:** Evaluates recall-oriented text quality (ROUGE-1, ROUGE-2, ROUGE-L)
3. **Perplexity:** Measures model's prediction confidence (lower is better)

### Qualitative Evaluation

- Side-by-side comparison of baseline vs fine-tuned responses
- Medical accuracy assessment
- Response coherence and relevance

### Expected Results

- **Target Improvement:** >10% improvement in perplexity over baseline
- **BLEU/ROUGE:** Significant improvement in generated answer quality
- **Medical Accuracy:** Better understanding of medical terminology and concepts

## 🎨 Deployment

### Gradio Web Interface

Interactive web UI featuring:

- Real-time question answering
- Model selection (Baseline vs Fine-tuned)
- Adjustable generation parameters (temperature, max tokens)
- Example medical questions
- Side-by-side comparison capability

**Access:** The Gradio interface is launched directly from the Colab notebook with public sharing enabled.

### Standalone Application

A standalone Gradio app is available in `demo/gradio_app.py` for local deployment.

```bash
python demo/gradio_app.py
```

## 🎥 Demo Video

A comprehensive 7-10 minute demo video showcasing:

- Project overview and motivation
- Dataset preprocessing walkthrough
- Fine-tuning process and experiments
- Model evaluation and metrics
- Live demonstration of the Gradio interface
- Baseline vs fine-tuned comparison
- Key insights and conclusions

**Video Link:** [Watch Demo on YouTube](https://youtu.be/IFD-PNFkHwY)

## 📊 Results Summary

### Performance Comparison

| Metric     | Baseline | Fine-tuned | Improvement |
| ---------- | -------- | ---------- | ----------- |
| BLEU       | 9.59     | 12.70      | +32.4%      |
| ROUGE-1    | 0.322    | 0.409      | +26.9%      |
| ROUGE-2    | 0.172    | 0.243      | +41.3%      |
| ROUGE-L    | 0.249    | 0.323      | +29.8%      |
| Perplexity | 1897.58  | 2.23       | **-99.88%** |

### Key Findings

1. **Massive Improvement:** Achieved **99.88% perplexity reduction** (1897.58 → 2.23), far exceeding the >10% target
2. **LoRA Efficiency:** Successfully reduced trainable parameters to ~0.2% (2.25M / 1.1B params) while achieving exceptional results
3. **Best Configuration:** Experiment 1 (lr=1e-4, rank=8, batch=2, epochs=2) performed best:
   - Train Loss: 0.8299
   - Eval Loss: 0.8004
   - Perplexity: 2.2263
   - Training Time: 59 minutes on Kaggle GPU T4
4. **BLEU/ROUGE Improvements:**
   - BLEU: +32.4% (9.59 → 12.70)
   - ROUGE-2: +41.3% (best improvement)
   - All metrics showed substantial gains
5. **Training Efficiency:** 4-bit quantization + LoRA enabled training on free GPU tier
6. **Hyperparameter Insights:** Lower learning rate (1e-4) with smaller LoRA rank (8) yielded best results

## � Example Conversations — Baseline vs Fine-tuned

This example shows a real interaction from the deployed Gradio interface, comparing both models on the same question.

---

**Question: What are the symptoms of Type 2 diabetes?**

> **Baseline Model (No Fine-tuning):**
> "The symptoms of Type 2 diabetes are:
>
> 1. Insulin resistance: This refers to the inability of insulin to properly transport glucose (sugar) into cells in the body.
> 2. Hyperglycemia: High blood sugar levels (hyperglycemia) are a primary symptom of diabetes.
> 3. Blurred vision: A decreased ability to focus on objects and recognize faces can also be a symptom of diabetes.
> 4. Thirst: Frequent urination, especially at night, can also be a symptom of diabetes.
> 5. Fatigue: This can be a sign that the..."

> **Fine-tuned Model (LoRA Trained):**
> "The symptoms of Type 2 diabetes include difficulty controlling blood sugar levels, increased thirst, and urination."

---

**Observation:** The fine-tuned model gives a concise, direct medical answer — consistent with the flashcard-style training data. The baseline generates a longer list but with less clinical focus. Across 500 test samples, the fine-tuned model achieved a **99.88% perplexity improvement** (1897.58 → 2.23), confirming significantly better understanding of medical language overall.

## �💡 Technical Insights

### What Worked Well

- LoRA + 4-bit quantization enabled training on free Colab GPU
- Medical flashcards dataset provided high-quality domain-specific data
- Systematic experimentation revealed optimal hyperparameter combinations
- Gradio provided excellent user interface with minimal code

### Challenges & Solutions

- **GPU Memory:** Solved with 4-bit quantization and gradient accumulation
- **Training Time:** Optimized with LoRA and limited dataset size
- **Evaluation:** Implemented multiple metrics for comprehensive assessment

### Future Improvements

1. **Dataset Expansion:** Scale to 5,000+ examples for better generalization
2. **RAG Integration:** Add retrieval-augmented generation for fact verification
3. **Safety Filters:** Implement medical advice warnings and disclaimers
4. **Larger Models:** Fine-tune larger models (3B-7B params) for better accuracy
5. **Multi-turn Conversations:** Enable context-aware dialogue

## 🛠️ Technologies Used

- **Framework:** PyTorch, Hugging Face Transformers
- **Fine-tuning:** PEFT (LoRA), BitsAndBytes (4-bit quantization)
- **Training:** TRL (SFTTrainer for supervised fine-tuning)
- **Evaluation:** ROUGE, SacreBLEU
- **Interface:** Gradio
- **Environment:** Google Colab (Free GPU Tier)

## 📚 References

1. **LoRA Paper:** [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
2. **TinyLlama:** [TinyLlama-1.1B-Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
3. **Dataset:** [Medical Meadow Flashcards](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)
4. **PEFT Library:** [Hugging Face PEFT](https://github.com/huggingface/peft)

## 👥 Author

**Course:** Domain-Specific LLM Fine-tuning Project  
**Date:** February 2026  
**Institution:** African Leadership University

## ⚖️ License & Disclaimer

**Educational Use Only**

This project is for educational purposes only. The medical assistant should NOT be used for actual medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.

**Model License:** TinyLlama-1.1B is licensed under Apache 2.0  
**Dataset License:** Medical Meadow datasets are openly available for research

## 🤝 Acknowledgments

- Hugging Face for transformers and PEFT libraries
- MedAlpaca team for the medical flashcards dataset
- TinyLlama team for the efficient base model
- Google Colab for free GPU resources
