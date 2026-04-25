import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/content/drive/MyDrive/housing.csv")

print(df.head())
print(df.info())

print("\nMissing values:\n", df.isnull().sum())

# Fill numerical columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical columns with mode
for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna(df[col].mode()[0])

le = LabelEncoder()
df['ocean_proximity'] = le.fit_transform(df['ocean_proximity'])

X = df[['longitude', 'latitude', 'housing_median_age',
        'total_rooms', 'total_bedrooms', 'population',
        'households', 'median_income', 'ocean_proximity']]

y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)


coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("\nFeature Coefficients:\n", coefficients)


print("\nOcean proximity categories:", le.classes_)

new_house = pd.DataFrame({
    'longitude': [-122.23],
    'latitude': [37.88],
    'housing_median_age': [20],
    'total_rooms': [2000],
    'total_bedrooms': [400],
    'population': [1000],
    'households': [300],
    'median_income': [5.0],
    'ocean_proximity': [le.transform([le.classes_[0]])[0]]
})

predicted_price = model.predict(new_house)

print("\nPredicted Price:", predicted_price[0])
