# Rede Bayesiana Simples para Previsão de Compras
# Este código implementa uma rede bayesiana simples para prever a probabilidade de um usuário realizar uma compra
# com base em três variáveis: histórico de compras, tempo no site e se clicou
# em uma promoção.

# Definição das variáveis e suas probabilidades condicionais

probabilidades = {
    "HistóricoCompras": {0: 0.7, 1: 0.3}, # 0: não tem histórico, 1: tem histórico
    "TempoNoSite": {0: 0.6, 1: 0.4}, # 0: pouco tempo, 1: muito tempo
    "ClicouEmPromocao": {0: 0.8, 1: 0.2}, # 0: não clicou, 1: clicou

    # Probabilidades de compra condicionadas às outras variáveis

    "Compra":{
        (0,0,0):0.1,
        (0,0,1):0.3,
        (0,1,0):0.2,
        (0,1,1):0.6,
        (1,0,0):0.4,
        (1,0,1):0.7,
        (1,1,0):0.8,
        (1,1,1):0.9
    }
}

# Função para calcular a probabilidade de compra com base nas evidências fornecidas
def calcular_probabilidade_compra(evidencias):
    historico = evidencias["HistóricoCompras"]
    tempo = evidencias["TempoNoSite"]
    promocao = evidencias["ClicouEmPromocao"]

# Verifica se as evidências estão dentro dos valores esperados
    prob_compra = probabilidades["Compra"][(historico, tempo, promocao)]
    prob_nao_compra = 1 - prob_compra

    return {"Comprar": prob_compra, "Não Comprar": prob_nao_compra}

# Exemplo de uso da rede bayesiana

evidencias = {
    "HistóricoCompras": 1,  # 0: Não Comprou, 1: Comprou
    "TempoNoSite": 0,       # 0: Curto, 1: Longo
    "ClicouEmPromocao": 1   # 0: Não Clicou, 1: Clicou
}

resultados = calcular_probabilidade_compra(evidencias)
print("Probabilidades de Compra:")
for resultado, probabilidade in resultados.items():
    print(f"{resultado}: {probabilidade:.2f}")