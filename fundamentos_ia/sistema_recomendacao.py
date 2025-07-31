# Sistema de Recomendação com A* para Produtos
# Este código implementa um sistema de recomendação de produtos utilizando o algoritmo A*.

# Importando bibliotecas necessárias

import heapq

# Definindo a classe Produto

class Produto:
    def __init__(self, nome, categoria, conversao_probabilidade):
        self.nome = nome
        self.categoria = categoria
        self.conversao_probabilidade = conversao_probabilidade

    def __repr__(self):
        return f"{self.nome} ({self.categoria})"
    
    def __eq__(self, other):
        return isinstance(other, Produto) and self.nome == other.nome
    
    def __hash__(self):
        return hash(self.nome)

# Definindo a classe AStarRecommendation

class AStarRecommendation:
    def __init__(self, produtos, heuristica):
        self.produtos = produtos
        self.heuristica = heuristica
        self.grafo = self._criar_grafo()

# Método para criar o grafo de produtos
    def _criar_grafo(self):
        grafo = {}
        for produto in self.produtos:
            grafo[produto] = [p for p in self.produtos if p != produto]
        return grafo

# Método A* para encontrar o caminho recomendado
    def a_star(self, inicio, objetivo):
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0 + self.heuristica(inicio), 0, inicio, [inicio]))
        visitados = set()

        while fila_prioridade:
            _, g, atual, caminho = heapq.heappop(fila_prioridade)

            if atual in visitados:
                continue

            visitados.add(atual)
            if atual == objetivo:
                return caminho

            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    h = self.heuristica(vizinho)
                    novo_caminho = caminho + [vizinho]
                    heapq.heappush(fila_prioridade, (g + 1 + h, g + 1, vizinho, novo_caminho))

        return []  # Se não houver caminho

# Definindo a heurística para o algoritmo A*
def heuristica(produto):
    return -produto.conversao_probabilidade

# Exemplo de uso do sistema de recomendação
produtos = [
    Produto("Produto A", "Categoria 1", 0.9),
    Produto("Produto B", "Categoria 1", 0.8),
    Produto("Produto C", "Categoria 2", 0.7),
    Produto("Produto D", "Categoria 2", 0.6),
]

recomendador = AStarRecommendation(produtos, heuristica)

inicio = produtos[0]  # Produto A
objetivo = produtos[2]  # Produto C

caminho_recomendado = recomendador.a_star(inicio, objetivo)

print("Caminho recomendado:")
for produto in caminho_recomendado:
    print(produto)