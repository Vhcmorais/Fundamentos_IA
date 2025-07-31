# Importando as bibliotecas 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Carregando o dataset
df = pd.read_csv("dataset_emocoes.csv")

# Converter o texto em string de letras minúsculas
df['texto'] = df['texto'].str.lower()

# Separar os dados em colunas: X (texto) e y (emoção)
X = df['texto']
y = df['emoção']

# Vetorização do texto para transformar em números
vetorizador = CountVectorizer()
X_vetor = vetorizador.fit_transform(X)

# Dividir os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X_vetor, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

########################################################################

# Função para prever a emoção de uma frase nova
def prever_emocao(frase):
    frase = frase.lower()
    frase_vetorizada = vetorizador.transform([frase])
    predicao = modelo.predict(frase_vetorizada)
    return predicao[0]

# Pede uma frase ao usuário e retorna a emoção prevista
print("Bem-vindo ao classificador de emoções!")
print("Digite uma frase e eu tentarei identificar a emoção associada.")

if __name__ == "__main__":
    while True:
        entrada = input("Digite uma frase para identificar a emoção: ")
        resultado = prever_emocao(entrada)
        print(f"Sentimento previsto: {resultado}")