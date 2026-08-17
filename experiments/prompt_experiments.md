# Prompt Engineering Experiment

## Objective

To understand how changes in prompt structure can influence the relevance, clarity, and format of an LLM response.

## Experiment

The same topic was used with three progressively detailed prompts.

### Prompt 1 — Basic

> Explain machine learning.

### Prompt 2 — Context

> Explain machine learning to a beginner who has basic programming knowledge. Use a simple real-world example.

### Prompt 3 — Structured

> Explain machine learning to a beginner who has basic programming knowledge.
>
> Requirements:
> - Maximum 100 words
> - Use one real-world example
> - Explain the basic idea clearly
> - Avoid mathematical terminology
> - Use bullet points

## Observations

The basic prompt allows the model to determine the response structure on its own.

Adding context provides information about the target audience and desired explanation style.

Adding explicit constraints provides greater control over the response length, structure, and level of technical detail.

## Key Learning

Prompt engineering involves designing instructions that provide sufficient context and constraints to guide an AI model toward a useful and consistent output.

Important prompt components can include:

- Context
- Task instructions
- Target audience
- Output format
- Length constraints
- Restrictions

## Conclusion

The experiment demonstrated that more specific prompts can provide greater control over the structure and relevance of LLM-generated responses.