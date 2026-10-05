# Exercício 5 – Parâmetro com valor padrão

# Crie uma função chamada criar_partida que receba:

# time_a
# time_b
# estadio

# O parâmetro estadio deve possuir o seguinte valor padrão:

# "Estádio Nacional"

# Depois, faça duas chamadas:

# Uma sem informar o estádio.
# Outra informando um estádio diferente.

def criar_partida(time_a: str, time_b: str, estadio: str = "Estádio Nacional") -> None:
    print(f"{time_a} x {time_b} -> {estadio}")

criar_partida("Grêmio", "Inter", "Arena do Grêmio")

criar_partida("Grêmio", "Inter")