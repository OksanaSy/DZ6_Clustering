import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score, calinski_harabasz_score

data = []
with open('combined.json', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

texts = [entry['contents'] for entry in data]

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=2, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans_labels = kmeans.fit_predict(tfidf_matrix)

print(f"Metrics for K-means with tf-idf:")
print(f"Adjusted Rand Index: {adjusted_rand_score(kmeans_labels, kmeans_labels):.2f}")
print(f"Silhouette Coefficient: {silhouette_score(tfidf_matrix, kmeans_labels):.2f}")
print(f"Calinski-Harabasz Index: {calinski_harabasz_score(tfidf_matrix.toarray(), kmeans_labels):.2f}")


'''
Metrics for K-means with tf-idf:
Adjusted Rand Index: 1.00
Silhouette Coefficient: 0.02
Calinski-Harabasz Index: 217.56
'''