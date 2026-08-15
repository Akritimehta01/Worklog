from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# Small example dataset
texts = [
    "I love this application",
    "This product is excellent",
    "The application is amazing",
    "This is a great product",
    "Very helpful and easy to use",
    "I really like this application",

    "I hate this application",
    "This product is terrible",
    "The application is awful",
    "This is a bad product",
    "Very poor and difficult to use",
    "I really dislike this application"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",

    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]


# Convert text into numerical TF-IDF features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.25,
    random_state=42
)


# Create and train the model
model = LogisticRegression()

model.fit(X_train, y_train)


# Make predictions on test data
predictions = model.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("ML Text Classification")
print("-" * 30)

print("\nTest Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Test the model on new examples
new_texts = [
    "This application is really helpful",
    "This product is horrible"
]

new_features = vectorizer.transform(new_texts)

new_predictions = model.predict(new_features)

print("\nNew Predictions:")

for text, prediction in zip(new_texts, new_predictions):
    print(f"{text} -> {prediction}")