# Experimental Results

This directory contains all the results from my fine-tuning experiments on the medical Q&A dataset.

## Directory Contents

### Main Results Files

- **experiment_results.csv** - Complete results table for all 4 experiments plus baseline
- **evaluation_metrics.json** - BLEU and ROUGE scores comparing baseline vs fine-tuned model
- **model_info.json** - Metadata about the best performing model (Experiment 1)

### Visualizations

- **baseline_vs_finetuned.png** - Side-by-side comparison showing 99.88% perplexity improvement
- **experiment_comparison.png** - Bar charts comparing all experiments across training loss, eval loss, perplexity, and training time

### Per-Experiment Directories

Each experiment directory (`experiment_1/` through `experiment_4/`) contains:

- Checkpoint folders with model states
- `trainer_state.json` - Training history and metrics
- `README.md` - Auto-generated training configuration

## Results Summary

| Experiment       | Learning Rate | LoRA Rank | Epochs | Perplexity  | Status       |
| ---------------- | ------------- | --------- | ------ | ----------- | ------------ |
| **Baseline**     | -             | -         | -      | **1897.58** | ✅ Reference |
| **Experiment 1** | 1e-4          | 8         | 2      | **2.2263**  | ✅ **BEST**  |
| **Experiment 2** | 5e-5          | 16        | 3      | **2.2531**  | ✅ Success   |
| **Experiment 3** | 2e-5          | 8         | 3      | NaN         | ❌ Failed    |
| **Experiment 4** | 1e-4          | 16        | 2      | NaN         | ❌ Failed    |

## Key Findings

### Best Model (Experiment 1)

- **Perplexity Improvement:** 99.88% reduction (1897.58 → 2.2263)
- **BLEU Score:** +32.4% improvement over baseline
- **ROUGE-2 Score:** +41.3% improvement over baseline
- **Training Time:** 59 minutes on Kaggle T4 GPU
- **GPU Memory:** ~8-9 GB VRAM

### Why Experiments 3 & 4 Failed

**Experiment 3 (lr=2e-5):** Learning rate was too small for 4-bit quantization. The gradient updates were smaller than the quantization noise, preventing the model from learning effectively.

**Experiment 4 (lr=1e-4, rank=16):** Too many parameters being updated aggressively with 4-bit precision caused numerical overflow. The combination of high learning rate and large LoRA rank exceeded the representable range.

### Lessons Learned

1. **QLoRA Fine-tuning** requires careful hyperparameter tuning - you can't use standard full-precision learning rates
2. **Sweet spot for 4-bit training:** lr=1e-4 with rank=8 balanced aggressive learning with numerical stability
3. **Higher LoRA rank ≠ better results** when working with quantized models
4. **Failed experiments are valuable** - they taught me about the constraints of low-precision training

## Evaluation Metrics Details

### BLEU Scores (Baseline → Fine-tuned)

- Baseline: 9.59
- Fine-tuned: 12.70
- Improvement: +32.4%

### ROUGE Scores (Baseline → Fine-tuned)

- ROUGE-1: 0.322 → 0.409 (+26.9%)
- ROUGE-2: 0.172 → 0.243 (+41.3%)
- ROUGE-L: 0.249 → 0.323 (+29.8%)

### Perplexity (Lower is Better)

- Baseline: 1897.58
- Fine-tuned (Best): 2.2263
- Reduction: 99.88%

## How to Use These Results

1. **For Analysis:** Review `experiment_results.csv` in a spreadsheet to compare hyperparameters
2. **For Visualization:** Open the PNG files to see graphical comparisons
3. **For Model Loading:** Use `model_info.json` to identify the best model path
4. **For Metrics:** Load `evaluation_metrics.json` to get detailed BLEU/ROUGE scores

## Training Resource Usage

All experiments were run on Kaggle's free T4 GPU (15GB VRAM):

- **Base Model Memory:** ~2.5 GB (with 4-bit quantization)
- **Per-Experiment Memory:** 8-11 GB VRAM depending on rank and batch size
- **Total Training Time:** ~4 hours for all experiments
- **Success Rate:** 50% (2 out of 4 experiments completed successfully)

The failed experiments weren't wasted time - they helped me understand the limits of QLoRA fine-tuning and why certain hyperparameter combinations work better with low-precision training.
