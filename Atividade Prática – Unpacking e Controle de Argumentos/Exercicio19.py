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

