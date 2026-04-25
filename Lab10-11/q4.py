import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/drive/MyDrive/Mall_Customers.csv')

df.columns = df.columns.str.strip()

print(df.columns)

df_features = df.drop(columns=['CustomerID'])

if 'Gender' in df_features.columns:
    df_features['Gender'] = df_features['Gender'].map({'Male': 0, 'Female': 1})
elif 'Genre' in df_features.columns:
    df_features['Genre'] = df_features['Genre'].map({'Male': 0, 'Female': 1})

kmeans_no_scale = KMeans(n_clusters=5, random_state=42)
df['Cluster_No_Scaling'] = kmeans_no_scale.fit_predict(df_features)

scaler = StandardScaler()

scaled_features = df_features.copy()

cols_to_scale = scaled_features.columns.tolist()
if 'Age' in cols_to_scale:
    cols_to_scale.remove('Age')

scaled_features[cols_to_scale] = scaler.fit_transform(scaled_features[cols_to_scale])

kmeans_scaled = KMeans(n_clusters=5, random_state=42)
df['Cluster_With_Scaling'] = kmeans_scaled.fit_predict(scaled_features)

print(df.head())
