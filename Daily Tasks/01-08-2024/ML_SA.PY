import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Create a simple dataset
data = [
    ("I love NLP", "Positive"),
    ("I HATE THIS TECHNOLOGY", "Negative"),
    ("It's okay, nothing special", "Neutral")
]

# Separate sentences and labels
sentences, labels = zip(*data)

# Download the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stopwords
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    # Remove stopwords and punctuation
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

# Preprocess the sentences
preprocessed_sentences = [preprocess(sentence) for sentence in sentences]

# Feature extraction
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(preprocessed_sentences)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.5, random_state=42)

# Train Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

# Predict labels for test data
y_pred = classifier.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
