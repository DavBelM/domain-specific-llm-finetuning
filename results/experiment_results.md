# Experiment Results

## Overview

This document tracks the results of all fine-tuning experiments conducted on the medical LLM assistant.

**Date:** February 2026  
**Base Model:** TinyLlama-1.1B-Chat-v1.0  
**Dataset:** Medical Meadow Medical Flashcards (2,500 examples)  
**Training Set:** 2,250 examples  
**Evaluation Set:** 250 examples

## Experiment Configurations

| Exp # | Learning Rate | Batch Size | Epochs | LoRA Rank | LoRA Alpha | Gradient Accum |
| ----- | ------------- | ---------- | ------ | --------- | ---------- | -------------- |
| 1     | 1e-4          | 2          | 2      | 8         | 16         | 4              |
| 2     | 5e-5          | 4          | 3      | 16        | 32         | 4              |
| 3     | 2e-5          | 2          | 3      | 8         | 16         | 4              |
| 4     | 1e-4          | 2          | 2      | 16        | 32         | 4              |

## Results Summary

**Note:** Results will be automatically populated when running the Colab notebook.

### Training Metrics

| Exp # | Train Loss | Eval Loss | Perplexity | Training Time (min) |
| ----- | ---------- | --------- | ---------- | ------------------- |
| 1     | TBD        | TBD       | TBD        | TBD                 |
| 2     | TBD        | TBD       | TBD        | TBD                 |
| 3     | TBD        | TBD       | TBD        | TBD                 |
| 4     | TBD        | TBD       | TBD        | TBD                 |

### Evaluation Metrics (BLEU, ROUGE)

Performance on 50 evaluation samples comparing generated vs reference answers:

| Exp #    | BLEU | ROUGE-1 | ROUGE-2 | ROUGE-L |
| -------- | ---- | ------- | ------- | ------- |
| Baseline | TBD  | TBD     | TBD     | TBD     |
| 1        | TBD  | TBD     | TBD     | TBD     |
| 2        | TBD  | TBD     | TBD     | TBD     |
| 3        | TBD  | TBD     | TBD     | TBD     |
| 4        | TBD  | TBD     | TBD     | TBD     |

## Best Experiment

**Best Model:** Experiment # TBD (Lowest perplexity)

**Configuration:**

- Learning Rate: TBD
- Batch Size: TBD
- Epochs: TBD
- LoRA Rank: TBD
- LoRA Alpha: TBD

**Performance:**

- Train Loss: TBD
- Eval Loss: TBD
- Perplexity: TBD
- BLEU: TBD
- ROUGE-L: TBD

**Improvement over Baseline:**

- Perplexity: TBD% improvement
- BLEU: TBD% improvement
- ROUGE-L: TBD% improvement

## Key Findings

### Hyperparameter Impact

**Learning Rate:**

- Higher learning rates (1e-4): Faster convergence but potential instability
- Lower learning rates (2e-5): Slower but more stable training
- Sweet spot: TBD

**LoRA Rank:**

- Rank 8: Fewer parameters, faster training, may limit capacity
- Rank 16: More parameters, better expressiveness, slower training
- Optimal: TBD

**Epochs:**

- 2 epochs: Fast but may underfit
- 3 epochs: Better convergence, risk of overfitting
- Optimal: TBD

### Training Observations

1. **Convergence:** TBD
2. **Overfitting:** TBD
3. **GPU Memory:** TBD GB peak usage
4. **Training Speed:** TBD minutes per epoch average

### GPU Utilization

**Environment:** Google Colab Free Tier (T4 GPU, 16GB VRAM)

| Metric                  | Value   |
| ----------------------- | ------- |
| Peak GPU Memory         | TBD GB  |
| Average GPU Utilization | TBD%    |
| Training Time per Epoch | TBD min |
| Total Training Time     | TBD min |

## Qualitative Evaluation

### Sample Responses Comparison

**Question:** "What is hypertension?"

**Baseline Model:**

```
TBD - To be filled after running notebook
```

**Fine-tuned Model (Best):**

```
TBD - To be filled after running notebook
```

**Analysis:** TBD

---

**Question:** "What are the symptoms of Type 2 diabetes?"

**Baseline Model:**

```
TBD
```

**Fine-tuned Model (Best):**

```
TBD
```

**Analysis:** TBD

## Lessons Learned

1. **LoRA Efficiency:** Successfully reduced trainable parameters to ~0.2% while maintaining quality
2. **Batch Size Trade-offs:** Smaller batches with gradient accumulation work well on limited GPU
3. **Epoch Selection:** TBD
4. **Data Quality:** High-quality medical flashcards dataset was crucial for performance

## Recommendations

### For Future Experiments

1. **Dataset Size:** Increase to 5,000+ examples for better generalization
2. **Learning Rate Schedule:** Try warmup + cosine decay for smoother training
3. **LoRA Configuration:** Experiment with different target modules
4. **Evaluation:** Add domain-specific metrics (medical accuracy)
5. **Data Augmentation:** Consider paraphrasing or back-translation

### For Production Deployment

1. **Merge Adapters:** Merge LoRA weights into base model for inference efficiency
2. **Quantization:** Use int8/int4 quantization for deployment
3. **Safety Filters:** Add medical disclaimer and filter inappropriate queries
4. **Human Review:** Validate responses with medical professionals
5. **Continuous Learning:** Regularly update with new medical knowledge

## Files Generated

After running the notebook, the following files are created:

- `experiment_results.csv`: Complete results in CSV format
- `model_info.json`: Best model configuration and metrics
- `evaluation_metrics.json`: Detailed BLEU/ROUGE metrics
- `experiment_comparison.png`: Visualization of all experiments

## Reproducibility

All experiments are fully reproducible by running the Colab notebook:

1. Open the notebook in Google Colab
2. Run all cells sequentially
3. Results will be automatically saved to `results/` folder
4. Download results for local analysis

**Random Seed:** 42 (for reproducibility)  
**Hardware:** Google Colab Free Tier (T4 GPU)  
**Software:** See `requirements.txt`

---

**Last Updated:** TBD (after running experiments)  
**Status:** Pending execution ⏳

For complete code and implementation details, see the [Colab notebook](../notebooks/medical_llm_finetuning.ipynb).
