import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt


df = pd.read_csv("/content/drive/MyDrive/marketing_campaign.csv", sep='\t')

print("Dataset Shape:", df.shape)
print(df.head())


features = [
    "Income", "Kidhome", "Teenhome",
    "Recency", "MntWines", "MntFruits",
    "MntMeatProducts", "MntFishProducts",
    "MntSweetProducts", "MntGoldProds"
]

df = df[features]

print("\nSelected Features:\n", df.columns)


for col in df.columns:
    df[col].fillna(df[col].median(), inplace=True)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)


inertia = []

K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)


plt.figure()
plt.plot(K_range, inertia, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")
plt.show()


kmeans = KMeans(n_clusters=4, random_state=42)

clusters = kmeans.fit_predict(X_scaled)

df['Cluster'] = clusters


plt.figure()
plt.scatter(df["Income"], df["MntWines"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.title("Customer Segments")
plt.show()


print("\nCluster Distribution:")
print(df['Cluster'].value_counts())

print("\nSample Data with Cluster Labels:")
print(df.head())
