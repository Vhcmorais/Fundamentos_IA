# Importar bibliotecas
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Carregar o dataset Diabetes
diabetes = load_diabetes()
X = diabetes.data  # Variáveis independentes
y = diabetes.target  # Variável dependente

# Dividir os dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Obter a importância das features
importances = model.feature_importances_
feature_names = diabetes.feature_names

# Criar um gráfico de barras para visualizar a importância das features
plt.figure(figsize=(10, 6))
plt.barh(feature_names, importances)
plt.title("Importância das Features")
plt.xlabel("Importância")
plt.ylabel("Feature")
plt.show()