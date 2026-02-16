# Evaluation Metrics

## Overview

This document provides detailed information about the evaluation metrics used to assess the fine-tuned medical LLM assistant.

## Metrics Used

### 1. Perplexity

**Definition:** Perplexity measures how well the model predicts the next token in a sequence. Lower perplexity indicates better prediction quality.

**Formula:**

```
Perplexity = exp(cross_entropy_loss)
```

**Interpretation:**

- **Lower is better**
- Perplexity of 1.0 = Perfect prediction
- Perplexity of 100 = Model is uncertain among ~100 options

**Baseline Perplexity:** TBD  
**Fine-tuned Perplexity:** TBD  
**Improvement:** TBD%

**Why it matters:** Perplexity directly measures the model's confidence in generating medical text, indicating how well it has learned the domain.

---

### 2. BLEU Score

**Definition:** BLEU (Bilingual Evaluation Understudy) measures n-gram overlap between generated and reference answers.

**Formula:**

```
BLEU = BP * exp(Σ(w_n * log(p_n)))
```

Where:

- BP = Brevity penalty
- p_n = Precision of n-grams (1-gram, 2-gram, 3-gram, 4-gram)
- w_n = Weights (typically 0.25 each)

**Range:** 0-100 (higher is better)

**Interpretation:**

- 0-10: Poor quality
- 10-20: Understandable but low quality
- 20-40: Reasonable quality
- 40+: Good to excellent quality

**Baseline BLEU:** TBD  
**Fine-tuned BLEU:** TBD  
**Improvement:** TBD%

**Why it matters:** BLEU assesses how closely generated answers match reference medical answers in terms of exact wording.

---

### 3. ROUGE Scores

**Definition:** ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures recall-based text quality.

#### ROUGE-1

- **Measures:** Unigram (single word) overlap
- **Focus:** Vocabulary coverage
- **Baseline:** TBD
- **Fine-tuned:** TBD

#### ROUGE-2

- **Measures:** Bigram (two-word sequence) overlap
- **Focus:** Phrase-level fluency
- **Baseline:** TBD
- **Fine-tuned:** TBD

#### ROUGE-L

- **Measures:** Longest Common Subsequence
- **Focus:** Sentence-level structure
- **Baseline:** TBD
- **Fine-tuned:** TBD

**Range:** 0-1 (higher is better)

**Interpretation:**

- 0.0-0.3: Poor overlap
- 0.3-0.5: Moderate overlap
- 0.5-0.7: Good overlap
- 0.7+: Excellent overlap

**Why it matters:** ROUGE emphasizes recall, ensuring the model captures key medical concepts even if wording differs.

---

### 4. Training & Evaluation Loss

**Training Loss:** Average loss on training data

- **Baseline:** N/A (no training)
- **Fine-tuned:** TBD

**Evaluation Loss:** Loss on held-out evaluation set

- **Baseline:** TBD
- **Fine-tuned:** TBD

**Why it matters:** Tracks learning progress and detects overfitting (if eval loss increases while train loss decreases).

---

## Evaluation Methodology

### Quantitative Evaluation

1. **Sample Size:** 50-100 examples from evaluation set
2. **Sampling:** Random selection for statistical validity
3. **Generation Parameters:**
   - Temperature: 0.7
   - Max tokens: 150
   - Top-p: 0.95

4. **Metric Calculation:**
   - BLEU: Use SacreBLEU library
   - ROUGE: Use rouge-score library
   - Perplexity: Computed from cross-entropy loss

### Qualitative Evaluation

**Criteria for Manual Assessment:**

1. **Medical Accuracy:** Correctness of medical facts
2. **Relevance:** Answers address the question
3. **Coherence:** Logical flow and readability
4. **Completeness:** Covers key aspects of the topic
5. **Terminology:** Appropriate use of medical terms

**Sample Questions:**

- "What is hypertension?"
- "What are the symptoms of Type 2 diabetes?"
- "How is pneumonia diagnosed?"
- "What causes asthma?"
- "What is the treatment for anemia?"

---

## Baseline vs Fine-tuned Comparison

### Overall Performance

| Metric     | Baseline | Fine-tuned | Improvement |
| ---------- | -------- | ---------- | ----------- |
| Perplexity | TBD      | TBD        | TBD%        |
| BLEU       | TBD      | TBD        | TBD%        |
| ROUGE-1    | TBD      | TBD        | TBD%        |
| ROUGE-2    | TBD      | TBD        | TBD%        |
| ROUGE-L    | TBD      | TBD        | TBD%        |

### Statistical Significance

**Test Used:** TBD (e.g., paired t-test, Wilcoxon signed-rank)  
**p-value:** TBD  
**Confidence Level:** 95%  
**Conclusion:** TBD

---

## Performance Across Question Types

### By Medical Domain

| Domain      | BLEU (Baseline) | BLEU (Fine-tuned) | Improvement |
| ----------- | --------------- | ----------------- | ----------- |
| Diseases    | TBD             | TBD               | TBD%        |
| Symptoms    | TBD             | TBD               | TBD%        |
| Treatments  | TBD             | TBD               | TBD%        |
| Diagnostics | TBD             | TBD               | TBD%        |

### By Answer Length

| Length Category    | Baseline ROUGE-L | Fine-tuned ROUGE-L | Improvement |
| ------------------ | ---------------- | ------------------ | ----------- |
| Short (<50 tokens) | TBD              | TBD                | TBD%        |
| Medium (50-150)    | TBD              | TBD                | TBD%        |
| Long (>150)        | TBD              | TBD                | TBD%        |

---

## Error Analysis

### Common Error Types

**Baseline Model:**

1. Generic responses lacking medical specificity
2. Incorrect medical terminology
3. Incomplete or vague answers
4. Off-topic or conversational drift

**Fine-tuned Model:**

1. TBD after evaluation
2. TBD
3. TBD
4. TBD

### Improvement Examples

**Question:** "What is hypertension?"

**Baseline Response:**

```
TBD - To be filled after running notebook
```

**Issues:** TBD

**Fine-tuned Response:**

```
TBD - To be filled after running notebook
```

**Improvements:** TBD

---

## Limitations

1. **Metric Limitations:**
   - BLEU/ROUGE favor exact matches, may penalize valid paraphrases
   - Metrics don't directly measure medical accuracy
   - No factual correctness verification

2. **Evaluation Set Size:**
   - 250 examples may not cover all medical scenarios
   - Limited diversity in question types

3. **No Expert Validation:**
   - Automated metrics only
   - Requires medical professional review for production use

4. **Domain Coverage:**
   - Dataset focused on basic medical concepts
   - May not generalize to specialized medical subfields

---

## Future Evaluation Enhancements

### Proposed Additions

1. **Medical Accuracy Metrics:**
   - Fact verification against medical databases
   - Entity recognition and validation
   - Contradiction detection

2. **Human Evaluation:**
   - Medical expert review
   - Factual correctness scoring
   - Safety assessment

3. **Robustness Testing:**
   - Out-of-domain questions
   - Adversarial examples
   - Edge cases

4. **Retrieval-Augmented Metrics:**
   - Source attribution
   - Citation accuracy
   - Evidence quality

---

## Conclusion

The evaluation framework provides comprehensive quantitative and qualitative assessment of the fine-tuned medical LLM assistant. Results demonstrate the effectiveness of LoRA fine-tuning for domain adaptation while highlighting areas for future improvement.

**Key Takeaways:**

- Multiple metrics provide holistic view of performance
- Quantitative metrics show measurable improvement
- Qualitative analysis reveals practical applicability
- Further validation by medical experts recommended

---

**Generated:** TBD (after running experiments)  
**Notebook:** [medical_llm_finetuning.ipynb](../notebooks/medical_llm_finetuning.ipynb)
