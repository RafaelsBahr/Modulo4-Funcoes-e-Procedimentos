# Exercício 6 – Mais de um valor padrão

# Crie uma função chamada registrar_jogador com os seguintes parâmetros:

# nome
# posicao="Não informada"
# titular=False

# A função deve mostrar os dados do jogador.

# Teste as seguintes chamadas:

# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)


# Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.

def registrar_jogador(nome: str, posicao: str = "Não informada", titular: bool = False) -> None:
    if titular:
        print(f"Nome do jogador(a): {nome} | Posição: {posicao} | É titular.")
    else:
        print(f"Nome do jogador(a): {nome} | Posição: {posicao} | Não é titular.")

registrar_jogador("Marta")
registrar_jogador("Marta", "Atacante")
registrar_jogador("Marta", "Atacante", True)

registrar_jogador("Marta", titular=True)