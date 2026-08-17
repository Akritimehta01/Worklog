def create_summary_prompt(text):
    """
    Create a structured prompt for summarizing text.
    """

    prompt = f"""
You are an AI assistant that summarizes technical content.

Summarize the following text for a software engineering student.

Requirements:
- Keep the summary under 100 words.
- Focus on the main technical concepts.
- Use simple and clear language.
- Do not introduce information that is not present in the text.

Text:
{text}
"""

    return prompt


if __name__ == "__main__":

    sample_text = """
    Machine learning is a branch of artificial intelligence that allows
    computer systems to learn patterns from data and make predictions
    without being explicitly programmed for every individual task.
    """

    prompt = create_summary_prompt(sample_text)

    print("Generated Prompt")
    print("-" * 30)
    print(prompt)