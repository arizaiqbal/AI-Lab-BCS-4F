import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("/content/drive/MyDrive/spam.csv")

print(df.head())
print(df.info())

# Convert labels: ham → 0, spam → 1
df['Category'] = df['Category'].map({'ham': 0, 'spam': 1})

# Handle missing values (just in case)
df['Message'] = df['Message'].fillna("")

# Text → Numerical (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

X = vectorizer.fit_transform(df['Message'])
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

def predict_email(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    
    return "Spam" if prediction == 1 else "Not Spam"

email1 = "Congratulations! You won a free ticket. Click now!"
email2 = "Hey, are we still meeting today?"

print("\nEmail 1:", predict_email(email1))
print("Email 2:", predict_email(email2))
