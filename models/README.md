# Model Information

## Base Model

**Name:** TinyLlama-1.1B-Chat-v1.0  
**Source:** [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)  
**License:** Apache 2.0

### Model Specifications

- **Parameters:** 1.1 Billion
- **Architecture:** Llama-based decoder-only transformer
- **Context Length:** 2048 tokens
- **Vocabulary Size:** 32,000 tokens
- **Training Data:** Mix of natural language and code (SlimPajama, StarCoder)

### Why TinyLlama?

1. **Colab Compatibility:** Small enough to fine-tune on free GPU (T4 with 16GB VRAM)
2. **Good Performance:** Despite small size, achieves reasonable quality
3. **Fast Training:** Quick iteration for experiments
4. **Chat Optimized:** Pre-trained on conversational data
5. **Open Source:** Fully accessible and modifiable

## Fine-tuning Method: LoRA

**PEFT (Parameter-Efficient Fine-Tuning) using LoRA**

### LoRA Configuration

```python
LoraConfig(
    r=8-16,                    # LoRA rank (low-rank matrices)
    lora_alpha=16-32,          # Scaling factor
    lora_dropout=0.1,          # Dropout for regularization
    bias="none",               # No bias training
    task_type="CAUSAL_LM",     # Causal language modeling
    target_modules=[           # Attention modules to adapt
        "q_proj",              # Query projection
        "k_proj",              # Key projection
        "v_proj",              # Value projection
        "o_proj"               # Output projection
    ]
)
```

### Memory Optimization

**4-bit Quantization (QLoRA):**

```python
BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
```

**Benefits:**

- Reduces model memory from ~4.4GB to ~1.1GB
- Enables training on free Colab GPU
- Minimal quality degradation
- 4x memory reduction

## Model Checkpoints

After running experiments, fine-tuned models are saved here:

```
models/
├── experiment_1/          # Experiment 1 checkpoint
│   ├── adapter_config.json
│   ├── adapter_model.bin
│   └── ...
├── experiment_2/          # Experiment 2 checkpoint
├── experiment_3/          # Experiment 3 checkpoint
└── experiment_4/          # Experiment 4 checkpoint
```

### Checkpoint Contents

Each experiment folder contains:

- `adapter_config.json`: LoRA configuration
- `adapter_model.bin`: LoRA weights (only ~8-16MB!)
- `pytorch_model.bin`: Full model state (if saved)
- `training_args.bin`: Training arguments
- `trainer_state.json`: Training state

### Loading a Fine-tuned Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device_map="auto"
)

# Load LoRA adapter
model = PeftModel.from_pretrained(
    base_model,
    "./models/experiment_1"
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)
```

## Model Size Comparison

| Component           | Size    |
| ------------------- | ------- |
| Base Model (FP32)   | ~4.4 GB |
| Base Model (4-bit)  | ~1.1 GB |
| LoRA Adapter (r=8)  | ~8 MB   |
| LoRA Adapter (r=16) | ~16 MB  |

**Key Insight:** LoRA adapters are tiny (8-16MB) compared to full model, making them easy to share and version control!

## Trainable Parameters

**Full Fine-tuning:** 1.1B parameters (100%)  
**LoRA Fine-tuning:** ~2-4M parameters (~0.2%)

Example output:

```
trainable params: 2,359,296 || all params: 1,102,359,296 || trainable%: 0.2140
```

## Model Performance

Performance varies by experiment. See `results/experiment_results.csv` for detailed metrics.

**Expected improvements:**

- Lower perplexity on medical questions
- Better medical terminology usage
- More accurate and concise answers
- Domain-specific knowledge retention

## Model Limitations

1. **Size Constraints:** 1.1B parameters limit complex reasoning
2. **Training Data:** Limited to 2,500 medical examples
3. **Context Window:** 2048 tokens may truncate long contexts
4. **Medical Accuracy:** Not validated by medical professionals
5. **General Knowledge:** May lose some general knowledge after fine-tuning

## Safety & Disclaimers

⚠️ **Important:** This model is for educational purposes only.

- **Not for Medical Use:** Do not use for diagnosis or treatment
- **Not Validated:** Not reviewed by medical professionals
- **May Hallucinate:** Can generate plausible but incorrect information
- **No Guarantees:** No warranty of accuracy or completeness

Always consult qualified healthcare professionals for medical advice.

## Version Control

**Note:** Model checkpoints are NOT committed to git due to size.

See `.gitignore`:

```
models/*/
!models/README.md
```

To share models:

- Upload to Hugging Face Hub
- Use git-lfs for version control
- Share via cloud storage (Google Drive, etc.)

## Model Citations

### Base Model

```bibtex
@misc{tinyllama,
  title={TinyLlama: An Open-Source Small Language Model},
  author={Zhang, Peiyuan and Guangtao, Zeng and Tianduo, Wang and Lu, Wei},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0}
}
```

### LoRA Method

```bibtex
@article{hu2021lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal={arXiv preprint arXiv:2106.09685},
  year={2021}
}
```

---

For more information, see the [main README](../README.md) or the [Colab notebook](../notebooks/medical_llm_finetuning.ipynb).
