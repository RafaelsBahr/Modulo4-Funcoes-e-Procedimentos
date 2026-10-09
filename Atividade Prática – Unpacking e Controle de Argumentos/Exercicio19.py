# Exercício 19 – Parâmetros somente nomeados com *

# Crie uma função chamada criar_jogador com a seguinte assinatura:

# def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...

# A função deve:

# Possuir uma docstring.
# Utilizar type hints.
# Utilizar um valor padrão para titular.
# Retornar uma string com os dados do jogador.
# O parâmetro nome pode ser informado por posição.

# Os parâmetros após * devem ser informados pelo nome.

# Faça uma chamada válida:

# jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
# print(jogador)

# Depois, faça outra chamada informando:

# titular=True

# Por fim, tente executar:

# criar_jogador("Marta","Atacante",10)

# Observe o erro e explique em um comentário por que posicao e numero não podem ser passados por posição.

def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:
    """
    Recebe dados dos jogadores e retorna str com todos dados
    
    Args:
        nome (str): Nome do jogador
        posicao (str): Posição
        numero (int): Numero camiseta
        titular (bool): Registra se é titular ou não
    Returns:
        (str): dados do jogador.
    """
    return (f"Nome: {nome}.\nPosição: {posicao}.\nNúmero: {numero}.\nTitular: {titular}")


jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
print(jogador)


jogador = criar_jogador("Marta",posicao="Atacante",numero=10,titular=True)
print(jogador)

# criar_jogador("Marta","Atacante",10)
# print(jogador)

# Tem erro na linha 52 porque a função exige argumentos nomeados a partir do segundo argumento (após "*"), e na linha 52 não são nomeados