from transformers import pipeline

# Carregar um modelo de geração de texto
gerador = pipeline("text-generation", model="gpt2")

# Definir prompt
prompt = "Qual a melhor época para visitar o Japão?"

# Gerar uma resposta ajustando os parâmetros para evitar repetições
resposta = gerador(
    prompt,
    max_length=50,      # Aumentar um pouco o comprimento
    temperature=0.7,    # Controla a aleatoriedade
    top_p=0.9,          # Faz a amostragem com núcleo (nucleus sampling)
    top_k=50,           # Restringe a escolha a top 50 palavras mais prováveis
    repetition_penalty=1.2 # Penaliza repetições
)

# Exibir resposta formatada
print(resposta[0]['generated_text'])