# Exercício 16 – Unpacking com ** e argumentos nomeados

# Considere o seguinte dicionário:

# jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}

# Crie uma função chamada apresentar_jogador que receba:

# nome
# idade
# posicao

# A função deve:

# Utilizar type hints em todos os parâmetros.
# Indicar através do type hint que a função não retorna nenhum valor.
# Possuir uma docstring.
# Exibir uma mensagem com os dados do jogador.

# Chame a função desempacotando o dicionário com **.

# Você não deve acessar manualmente:

# jogador["nome"]
# jogador["idade"]
# jogador["posicao"]

# Depois, responda em um comentário no código:

# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}

def apresentar_jogador(nome: str, idade: int, posicao: str) -> None:
    """
    Recebe dados e imprime os dados do jogador.

    Args:
        nome (str): Nome do jogador(a)
        idade (int): Idade do jogador(a)
        posicao (str): Posicao do jogador(a)
    """
    print(f"{nome} tem {idade} anos e joga como {posicao}")

apresentar_jogador(**jogador)

# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?
# Porque o desempacotamento com ** usa argumentos nomeados