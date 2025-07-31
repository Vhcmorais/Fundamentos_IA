# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Criando conjuntos de dados simulados
np.random.seed(42)
X = 2.5 * np.random.randn(100, 1) + 25  # Tamanho do imóvel
y = 500 + (X * 20) + np.random.randn(100, 1) * 10  # Preço do imóvel

# Definindo features e labels
features = X
labels = y

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)

#Modelo de regressão linear
# Y = A X + B
# Y -> Variável de saída
# X -> Tamanho do imóvel
# A e B são coeficientes

# Coeficientes da regressão
print(f"Coeficiente angular (b1): {model.coef_[0][0]:.2f}")
print(f"Intercepto (b0): {model.intercept_[0]:.2f}")

# Predições nos dados de teste
y_pred = model.predict(X_test)

# Indicadores da Avaliação do modelo no conjunto de teste

#R² ajuste dos dados ao modelo
r2 = r2_score(y_test, y_pred)
#MAE (Erro Médio Absoluto)
mae = mean_absolute_error(y_test, y_pred)
#RMSE (Raiz do Erro Quadrático Médio)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\nMétricas de avaliação:")
print(f"R² no teste: {r2:.2f}")
print(f"Erro Médio Absoluto (MAE): {mae:.2f}")
print(f"Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f}")

# Avaliação cruzada
cv_scores = cross_val_score(model, features, labels, cv=5, scoring='r2')
print(f"\nMédia dos scores de validação cruzada: {cv_scores.mean():.2f}")

# Gráfico da reta de regressão
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Dados reais')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regressão Linear')
plt.xlabel("Tamanho do imóvel")
plt.ylabel("Preço do imóvel")
plt.title("Regressão Linear: Preço x Tamanho do Imóvel")
plt.legend()
plt.show()