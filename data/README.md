# Dataset Information

## Primary Dataset

**Name:** Medical Meadow Medical Flashcards  
**Source:** [medalpaca/medical_meadow_medical_flashcards](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)  
**License:** Open for research and educational use

### Dataset Description

The Medical Meadow Medical Flashcards dataset contains medical question-answer pairs designed for medical education. It covers a wide range of medical topics including:

- **Diseases & Conditions:** Definitions, causes, symptoms
- **Treatments:** Medications, procedures, therapies
- **Anatomy & Physiology:** Body systems, organs, functions
- **Medical Terminology:** Common medical terms and concepts
- **Diagnostics:** Tests, procedures, interpretations

### Dataset Statistics

- **Total Examples:** ~33,000+ medical flashcards
- **Used in Project:** 2,500 carefully selected examples
- **Train Set:** 2,250 examples (90%)
- **Eval Set:** 250 examples (10%)

### Data Format

Each example contains:

- `input`: Medical question or prompt
- `output`: Corresponding answer or explanation

**Example:**

```json
{
  "input": "What is hypertension?",
  "output": "Hypertension, also known as high blood pressure, is a condition where the force of blood against artery walls is consistently too high. It is typically defined as blood pressure readings of 140/90 mmHg or higher."
}
```

### Data Quality

**Inclusion Criteria:**

- Clear, well-formed questions
- Accurate, concise answers
- Minimum length: 10 characters for both input and output
- Maximum length: 1000 characters (input), 2000 characters (output)

**Exclusion Criteria:**

- Empty or missing fields
- Duplicate question-answer pairs
- Overly short or uninformative responses
- Extremely long or complex responses

### Preprocessing Pipeline

1. **Loading:** Load dataset from Hugging Face
2. **Cleaning:** Remove extra whitespace, normalize text
3. **Filtering:** Apply quality filters (length, completeness)
4. **Deduplication:** Remove exact duplicates
5. **Sampling:** Select 2,500 diverse examples
6. **Formatting:** Convert to instruction-response format
7. **Splitting:** 90/10 train-test split

### Data Access

The dataset is automatically downloaded when running the Colab notebook:

```python
from datasets import load_dataset
dataset = load_dataset("medalpaca/medical_meadow_medical_flashcards")
```

### Citation

If you use this dataset, please cite the MedAlpaca project:

```bibtex
@misc{medalpaca,
  author = {MedAlpaca Team},
  title = {Medical Meadow: Medical Flashcards Dataset},
  year = {2023},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards}
}
```

## Alternative Datasets (Not Used)

Other medical datasets that were considered:

1. **MedQA:** Medical question answering dataset
2. **PubMedQA:** Biomedical research questions
3. **HealthSearchQA:** Consumer health questions
4. **MIMIC-III:** Clinical notes (requires credentialing)

## Data Storage

**Important:** Due to size constraints, the processed dataset is not stored in this repository. The notebook downloads and preprocesses data automatically.

**Processed data location (after running notebook):**

- Cached in Colab runtime (temporary)
- Not committed to git (see `.gitignore`)

## Data Privacy & Ethics

- **No PHI:** Dataset contains no Protected Health Information
- **No Patient Data:** All examples are educational, not from real patients
- **Educational Use:** Dataset is for learning purposes only
- **No Medical Advice:** Output should not be used for actual medical decisions

---

For questions about the dataset, please refer to the [Hugging Face dataset page](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards).
