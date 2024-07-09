import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score, calinski_harabasz_score

data = []
with open('combined.json', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

texts = [entry['contents'] for entry in data]

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=2, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

num_topics = 3
svd = TruncatedSVD(n_components=num_topics, random_state=42)
svd_matrix = svd.fit_transform(tfidf_matrix)

kmeans = KMeans(n_clusters=num_topics, random_state=42)
kmeans_labels = kmeans.fit_predict(svd_matrix)

print(f"Metrics for LSA with K-means:")
print(f"Adjusted Rand Index: {adjusted_rand_score(kmeans_labels, kmeans_labels):.2f}")
print(f"Silhouette Coefficient: {silhouette_score(svd_matrix, kmeans_labels):.2f}")
print(f"Calinski-Harabasz Index: {calinski_harabasz_score(svd_matrix, kmeans_labels):.2f}")


'''
Metrics for LSA with K-means:
Adjusted Rand Index: 1.00
Silhouette Coefficient: 0.72
Calinski-Harabasz Index: 26503.86
'''