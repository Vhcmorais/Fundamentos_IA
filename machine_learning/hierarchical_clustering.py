from sklearn.datasets import load_iris
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Carregar o dataset Iris
iris = load_iris()
X = iris.data

# Normalizar os dados para melhorar a performance do clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Criar o dendrograma
plt.figure(figsize=(10, 5))
sch.dendrogram(sch.linkage(X_scaled, method='ward'))
plt.title("Dendrograma do Agrupamento Hierárquico")
plt.xlabel("Amostras")
plt.ylabel("Distância Euclidiana")
plt.show()

###################################

# Categorizar o agrupamento hierárquico

from sklearn.cluster import AgglomerativeClustering

# Aplicar Hierarchical Clustering definindo 3 grupos
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
clusters = hc.fit_predict(X_scaled)

# Visualizar os clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.title("Agrupamento com Hierarchical Clustering")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()