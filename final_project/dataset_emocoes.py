# Criando meu dataset usado como repositório padrão de treinamento
# para a IA

# Importando as bibliotecas
import pandas as pd

# Definindo dados como "texto" e "emoção"
dados = [
    
    # Felicidade
    ("Hoje é meu aniversário, estou muito feliz!", "felicidade"),
    ("Estou tão grato por ter amigos incríveis.", "felicidade"),
    ("Estou tão apaixonado por esta música!", "felicidade"),
    ("Ganhei um presente inesperado hoje, estou radiante!", "felicidade"),
    ("Não esperava ver você aqui, que surpresa boa!", "felicidade"),
    ("Sou muito grato pela ajuda que recebi hoje.", "felicidade"),
    ("Estou pulando de alegria com essa notícia maravilhosa!", "felicidade"),
    ("Finalmente consegui aquela promoção que queria!", "felicidade"),
    ("Adorei passar tempo com minha família hoje.", "felicidade"),
    ("Sinto que tudo está dando certo na minha vida.", "felicidade"),
    
    # Tristeza
    ("Estou tão triste hoje, não sei o que fazer.", "tristeza"),
    ("Nada parece dar certo ultimamente, me sinto vazio.", "tristeza"),
    ("Não entendo por que tudo mudou de repente.", "tristeza"),
    ("Hoje acordei com uma tristeza que não consigo explicar.", "tristeza"),
    ("Sinto falta das pessoas que se foram.", "tristeza"),
    ("Não tenho vontade de fazer nada ultimamente.", "tristeza"),
    ("Meu coração está pesado de tanta dor.", "tristeza"),
    ("Me sinto sozinho mesmo quando estou rodeado de gente.", "tristeza"),
    ("Perdi algo que eu amava muito.", "tristeza"),
    ("Nada me anima mais como antes.", "tristeza"),
    
    # Ansiedade
    ("Estou tão ansioso para o fim de semana!", "ansiedade"),
    ("Estou tão confuso sobre o que fazer a seguir.", "ansiedade"),
    ("A entrevista de amanhã está me deixando agitado.", "ansiedade"),
    ("Estou contando os minutos para a viagem, mal posso esperar!", "ansiedade"),
    ("Não vejo a hora do fim de semana chegar!", "ansiedade"),
    ("Estou contando os minutos para a viagem, mal posso esperar!", "ansiedade"),
    ("Nem acredito que a prova é amanhã, estou tão nervoso!", "ansiedade"),
    ("Não vejo a hora de encontrar meus amigos de novo.", "ansiedade"),
    ("Estou ansioso para saber o resultado do meu exame.", "ansiedade"),
    
    # Raiva
    ("Estou tão irritado com o trânsito que não aguento mais!", "raiva"),
    ("Erraram meu pedido pela terceira vez, que absurdo!", "raiva"),
    ("Não acredito que fizeram isso comigo, estou revoltado!", "raiva"),
    ("Essa situação injusta está me deixando muito frustrado.", "raiva"),
    ("Isso me deixou realmente furioso, não quero saber de conversa.", "raiva"),
    ("Não suporto quando as pessoas não cumprem a palavra, me tira do sério.", "raiva"),
    ("Sinto vontade de gritar só de lembrar do que aconteceu.", "raiva"),
    ("Estou cansado de tanta desonestidade e falta de respeito.", "raiva"),
    ("Essa situação me tira do sério, não sei mais o que fazer.", "raiva"),
    ("Quero resolver isso agora, estou realmente revoltado.", "raiva"),

]

# Definindo o dataset para colunas de dados e convertendo .py em .csv
df = pd.DataFrame(dados, columns=["texto", "emoção"])
df.to_csv("dataset_emocoes.csv", index=False, encoding="utf-8")

#Saída de sucesso!
print("Dataset criado com sucesso!")