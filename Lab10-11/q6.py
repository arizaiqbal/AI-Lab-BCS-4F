import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [3.5, 2.8, 3.9, 1.8, 2.5, 3.2, 3.8, 2.0, 2.9, 3.6],
    'study_hours': [15, 8, 20, 5, 10, 12, 18, 6, 9, 16],
    'attendance_rate': [90, 70, 95, 60, 75, 85, 92, 65, 80, 88]
}

df = pd.DataFrame(data)

X = df[['GPA', 'study_hours', 'attendance_rate']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []

for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(2,7), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print(df)

plt.scatter(df['study_hours'], df['GPA'], c=df['Cluster'])
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.title('Student Clusters')
plt.show()
