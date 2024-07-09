import numpy as np
from sklearn.metrics import adjusted_rand_score, silhouette_score, calinski_harabasz_score

np.random.seed(42)
num_objects = 100
random_labels = np.random.randint(0, 3, size=num_objects)


print(f"Metrics for Random Clustering:")
print(f"Adjusted Rand Index: {adjusted_rand_score(random_labels, random_labels):.2f}")
print(f"Silhouette Coefficient: {silhouette_score(random_labels.reshape(-1, 1), random_labels):.2f}")
print(f"Calinski-Harabasz Index: {calinski_harabasz_score(random_labels.reshape(-1, 1), random_labels):.2f}")

'''
Metrics for Random Clustering:
Adjusted Rand Index: 1.00
Silhouette Coefficient: 1.00
Calinski-Harabasz Index: 1.00
'''