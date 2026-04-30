
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error

import matplotlib.pyplot as plt

df = pd.read_csv("/content/drive/MyDrive/train (1).csv")

print("Dataset Shape:", df.shape)
print(df.head())

missing = df.isnull().sum()
missing = missing[missing > 0]

print("\nMissing Values:\n", missing.sort_values(ascending=False).head(10))

for col in df.columns:
    if df[col].dtype == "object":
        # categorical
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        # numerical
        df[col].fillna(df[col].median(), inplace=True)


df = pd.get_dummies(df, drop_first=True)

print("\nAfter Encoding Shape:", df.shape)

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)

def evaluate_model(name, y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"\n===== {name} =====")
    print("MAE  :", mae)
    print("RMSE :", rmse)
    
    return mae, rmse

lr_mae, lr_rmse = evaluate_model("Linear Regression", y_test, y_pred_lr)
dt_mae, dt_rmse = evaluate_model("Decision Tree", y_test, y_pred_dt)

# Creating a small comparison table
comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "LR Predicted": y_pred_lr,
    "DT Predicted": y_pred_dt
})

print("\nSample Predictions:\n")
print(comparison.head(10))


plt.figure()

# Scatter plot for Linear Regression
plt.scatter(y_test, y_pred_lr, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Linear Regression: Actual vs Predicted")

plt.show()


print("\nFINAL CONCLUSION")

if dt_rmse < lr_rmse:
    print("Decision Tree performed better (lower RMSE).")
else:
    print("Linear Regression performed better (lower RMSE).")

print("\nNote:")
print("Lower MAE and RMSE indicate better model performance.")
