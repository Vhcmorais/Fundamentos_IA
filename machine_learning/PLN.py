from sklearn.feature_extraction.text import CountVectorizer

# Conjunto de frases
frases = ["Eu amo viajar para o Japão", "Viajar é incrível", "Quero conhecer o Japão"]

# Criando o modelo BoW
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

# Exibir matriz resultante
print(vectorizer.get_feature_names_out())
print(X.toarray())