import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

df['vehicle_type'] = df['vehicle_type'].astype('category').cat.codes

features = df.drop(columns=['vehicle_serial_no'])

kmeans_no_scale = KMeans(n_clusters=3, random_state=42)
df['Cluster_No_Scaling'] = kmeans_no_scale.fit_predict(features)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['Cluster_With_Scaling'] = kmeans_scaled.fit_predict(scaled_features)

print(df)
