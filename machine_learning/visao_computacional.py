from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
import cv2
from google.colab import files
from PIL import Image

# Fazer upload da imagem
uploaded = files.upload()
imagem_path = list(uploaded.keys())[0]  # Pega o nome do arquivo enviado

# Carregar a imagem usando OpenCV
imagem = cv2.imread(imagem_path)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Carregar o modelo MobileNetV2 pré-treinado
modelo = MobileNetV2(weights="imagenet")

# Pré-processar a imagem para o formato esperado pelo modelo
imagem_redimensionada = cv2.resize(imagem_rgb, (224, 224))
imagem_array = np.expand_dims(imagem_redimensionada, axis=0)
imagem_array = preprocess_input(imagem_array)

# Fazer a previsão
predicoes = modelo.predict(imagem_array)
label = decode_predictions(predicoes)
print("Objeto identificado:", label[0][0][1])  # Exibe a classe identificada