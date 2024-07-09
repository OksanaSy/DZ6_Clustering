# DZ6_Clustering

Модель 1: K-means з tf-idf
    Adjusted Rand Index: 1.00
    Silhouette Coefficient: 0.02
    Calinski-Harabasz Index: 217.56
Модель 2: LSA з K-means
    Adjusted Rand Index: 1.00
    Silhouette Coefficient: 0.72
    Calinski-Harabasz Index: 26503.86
Модель 3: Випадкова кластеризація
    Adjusted Rand Index: 1.00
    Silhouette Coefficient: 1.00
    Calinski-Harabasz Index: 1.00

Інтерпретація результатів:

Adjusted Rand Index (ARI):
Всі три моделі мають ARI рівний 1.0, що вказує на ідеальну узгодженість зі золотим стандартом.

Silhouette Coefficient:
Модель LSA з K-means має значно вищий Silhouette Coefficient (0.72), що свідчить про кращу якість кластеризації та кращу внутрішню гомогенність кластерів порівняно з іншими моделями.
Модель випадкової кластеризації також має високий Silhouette Coefficient (1.00), але це відбувається через випадковий призначення лейблів, тому цей результат не є інформативним для оцінки реальної якості кластеризації.

Calinski-Harabasz Index:
Модель LSA з K-means має найвище значення Calinski-Harabasz Index (26503.86), що підкріплює її ефективність в утворенні чітких і відокремлених кластерів.
Модель K-means з tf-idf має помірне значення індексу (217.56), що свідчить про адекватність кластеризації, але меншу відокремленість кластерів порівняно з LSA.
Випадкова кластеризація має найнижче значення Calinski-Harabasz Index (1.00), що є очікуваним результатом для випадкової моделі.

Висновок:
Модель, яка використовує LSA з K-means, демонструє кращі результати за Silhouette Coefficient та Calinski-Harabasz Index порівняно з K-means з tf-idf. Випадкова кластеризація, хоча має високий Silhouette Coefficient, не є надійною для реальних даних через випадкове призначення лейблів.
