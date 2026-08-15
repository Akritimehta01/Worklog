def preprocess_text(text):
    """
    Clean and normalize input text.
    """
    text = text.lower()
    text = text.strip()

    return text


def classify_text(text):
    """
    Perform simple sentiment classification
    using predefined positive and negative words.
    """

    positive_words = {
        "good",
        "great",
        "excellent",
        "amazing",
        "awesome",
        "love",
        "helpful"
    }

    negative_words = {
        "bad",
        "poor",
        "terrible",
        "awful",
        "hate",
        "useless"
    }

    words = text.split()

    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "positive_matches": positive_count,
        "negative_matches": negative_count
    }


def run_pipeline(text):
    """
    Execute the complete text analysis pipeline.
    """

    processed_text = preprocess_text(text)

    result = classify_text(processed_text)

    return {
        "input": text,
        "processed_text": processed_text,
        "result": result
    }


def evaluate_pipeline(test_cases):
    """
    Evaluate the pipeline using predefined test cases.
    """

    correct = 0

    for text, expected in test_cases:
        output = run_pipeline(text)

        predicted = output["result"]["sentiment"]

        if predicted == expected:
            correct += 1

        print(f"\nInput: {text}")
        print(f"Expected: {expected}")
        print(f"Predicted: {predicted}")

    accuracy = correct / len(test_cases)

    return accuracy


if __name__ == "__main__":

    test_cases = [
        ("This application is excellent and helpful", "Positive"),
        ("The application is terrible and useless", "Negative"),
        ("The application is okay", "Neutral"),
        ("I love this application", "Positive"),
        ("This product is awful", "Negative")
    ]

    print("AI Text Analysis Pipeline")
    print("-" * 30)

    accuracy = evaluate_pipeline(test_cases)

    print("\nEvaluation Accuracy:", accuracy)