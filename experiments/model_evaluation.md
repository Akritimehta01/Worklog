# Model Evaluation Experiment

## Objective

The objective of this experiment was to explore and compare two approaches for basic text sentiment classification:

1. A rule-based classification approach.
2. A machine learning-based classification approach.

The experiment was designed to understand the differences between manually defined rules and a model trained on labelled text data.

---

## 1. Rule-Based Baseline

The initial implementation used predefined positive and negative words.

The pipeline:

1. Receives text input.
2. Converts the text to lowercase.
3. Splits the text into individual words.
4. Counts positive and negative word matches.
5. Assigns a sentiment label based on the number of matches.

### Example

```text
Input:
"This application is excellent and helpful"

Positive matches:
excellent, helpful

Prediction:
Positive