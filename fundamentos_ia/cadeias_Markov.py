# Cadeias de Markov para previsão do tempo
# Este script implementa um modelo de Cadeias de Markov para prever o tempo
# com base em estados anteriores. A matriz de transição define as probabilidades


# importação de bibliotecas necessárias

import numpy as np

# inicialização dos estados e da matriz de transição

states = ["Ensolarado", "Nublado", "Chuvoso"]

transition_matrix = [
    [0.8, 0.15, 0.05],
    [0.2, 0.6, 0.2],
    [0.25, 0.25, 0.5]
]

# definição do estado inicial e do número de dias a serem previstos

initial_state = "Ensolarado"

num_days = 10

# função para prever o tempo usando a Cadeia de Markov

def get_state_index(state):
    return states.index(state)

def predict_weather(initial_state, num_days):
    current_state = initial_state
    forecast = [current_state]

    for _ in range(num_days - 1):
        current_index = get_state_index(current_state)
        next_state= np.random.choice(
            states,
            p=transition_matrix[current_index])
        forecast.append(next_state)
        current_state = next_state

    return forecast

# previsão do tempo

forecast = predict_weather(initial_state, num_days)

print(f"Previsão inicial: {initial_state}")
print("Previsão do tempo para os próximos dias:")
for day, state in enumerate(forecast, start=1):
    print(f"Dia {day}: {state}")
     