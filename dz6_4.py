import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=100, centers=3, cluster_std=1.0, random_state=42)

inertia_values = []

k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia_values.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_values, marker='o', linestyle='-', color='b')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.xticks(k_range)
plt.grid(True)

optimal_k = None
for i in range(1, len(inertia_values)):
    if inertia_values[i] - inertia_values[i-1] < 0.1:
        optimal_k = i
        break

if optimal_k is not None:
    print(f'Optimal number of clusters (k): {optimal_k}')
else:
    print('Optimal number of clusters could not be determined.')

plt.show()
