import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv(
    "/content/drive/MyDrive/OnlineRetail.csv",
    encoding='ISO-8859-1',
    engine='python'
)

print(df.head())
print(df.info())

df = df.dropna(subset=['CustomerID'])

df = df[df['Quantity'] > 0]

# Create total spending per row
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


customer_df = df.groupby('CustomerID').agg({
    'TotalPrice': 'sum',
    'InvoiceNo': 'nunique',
    'Quantity': 'sum'
}).reset_index()

customer_df.rename(columns={
    'TotalPrice': 'total_spending',
    'InvoiceNo': 'visits',
    'Quantity': 'total_items'
}, inplace=True)

print("\nCustomer Dataset:\n", customer_df.head())

threshold = customer_df['total_spending'].quantile(0.70)

customer_df['customer_type'] = np.where(
    customer_df['total_spending'] >= threshold, 1, 0
)

print("\nLabel distribution:\n", customer_df['customer_type'].value_counts())


X = customer_df[['total_spending', 'visits', 'total_items']]
y = customer_df['customer_type']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_model = SVC(kernel='linear')
svm_model.fit(X_train_scaled, y_train)

svm_pred = svm_model.predict(X_test_scaled)

tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)

rules = export_text(tree_model, feature_names=list(X.columns))

print("\nDECISION TREE RULES:\n")
print(rules)


print("\n==================== SVM RESULTS ====================")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

print("\n================ DECISION TREE RESULTS ================")
print("Accuracy:", accuracy_score(y_test, tree_pred))
print(classification_report(y_test, tree_pred))
