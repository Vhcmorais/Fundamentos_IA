import numpy as np
import gymnasium as gym

# Inicializar o ambiente FrozenLake
# O agente precisa atravessar um lago congelado sem cair nos buracos
env = gym.make("FrozenLake-v1", is_slippery=True)

# Definir os hiperparâmetros do Q-Learning
alpha = 0.8  # Taxa de aprendizado: o quanto o agente aprende de novas informações
gamma = 0.95  # Fator de desconto: quão importante são as recompensas futuras em comparação com as imediatas
epsilon = 1.0  # Probabilidade inicial de explorar ações aleatórias
epsilon_decay = 0.999  # Reduz gradualmente a exploração conforme o agente aprende
epsilon_min = 0.01  # Limite mínimo de exploração para garantir que o agente ainda explore um pouco
num_episodes = 20000  # Número total de tentativas de aprendizado (episódios)

# Criar a tabela Q (Q-table) com zeros
# As linhas representam os estados e as colunas representam as ações
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Iniciar o treinamento do agente
for episode in range(num_episodes):
    # Reiniciar o ambiente a cada episódio
    state, _ = env.reset()
    done = False

    while not done:
        # Escolher uma ação usando a estratégia epsilon-greedy
        # Com probabilidade 'epsilon', escolhemos uma ação aleatória (exploração)
        # Caso contrário, escolhemos a melhor ação conhecida até o momento (exploração)
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explorar uma ação aleatória
        else:
            action = np.argmax(q_table[state])  # Explorar a ação com maior valor na Q-table

        # Executar a ação escolhida no ambiente
        next_state, reward, done, truncated, _ = env.step(action)

        # Atualizar a Q-table com a fórmula de aprendizado por reforço
        # Q(s, a) = Q(s, a) + alpha * (recompensa + desconto * max(Q(s', a')) - Q(s, a))
        best_next_action = np.max(q_table[next_state])  # Melhor ação no próximo estado
        q_table[state, action] += alpha * (reward + gamma * best_next_action - q_table[state, action])

        # Avançar para o próximo estado
        state = next_state

    # Reduzir a taxa de exploração gradualmente, sem ultrapassar o mínimo definido
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Avaliar o desempenho do agente treinado
# Aqui, testamos 1000 episódios para verificar quantas vezes ele atravessa o lago com sucesso
successes = 0
for episode in range(1000):
    state, _ = env.reset()
    done = False
    while not done:
        # O agente agora só escolhe a melhor ação aprendida (sem exploração aleatória)
        action = np.argmax(q_table[state])
        state, reward, done, truncated, _ = env.step(action)
        if done and reward == 1.0:
            successes += 1  # Contabilizar os sucessos

# Exibir o resultado final
print(f"O agente conseguiu atravessar o lago com sucesso em {successes} de 1000 episódios.")