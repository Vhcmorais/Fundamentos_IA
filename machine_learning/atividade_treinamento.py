import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dataset = datasets.load_iris()

df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

X = df.iloc[:, :-1]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

cross_val_scores = cross_val_score(model, X, y, cv=5)
print(f'Acurácia média na validação cruzada: {cross_val_scores.mean():.2f}')

nova_amostra = np.array([[5.1, 3.5, 1.4, 0.2]])
predicao = model.predict(nova_amostra)
print(f'Classe prevista para a nova amostra: {dataset.target_names[predicao[0]]}')

amostras_testes = np.array([
    [5.0, 3.5, 1.4, 0.2],
    [6.0, 2.2, 4.0, 1.0],
    [6.5, 3.0, 5.2, 2.0]])

predicoes = model.predict(amostras_testes)

for i, pred in enumerate(predicoes):
  print(f"Amostra {i+1} -> Classe prevista: {dataset.target_names[pred]}")