# Exercício 1 – Argumentos posicionais

# Crie uma função chamada apresentar_jogador que receba:

# nome
# posicao
# A função deve exibir uma mensagem semelhante a:

# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.

def apresentar_jogador(nome: str, posicao: str) -> None:
    print(f"Jogador: {nome} | Posição: {posicao}")

apresentar_jogador("Marta", "Atacante")

# Exemplo:

# apresentar_jogador("Marta", "Atacante")