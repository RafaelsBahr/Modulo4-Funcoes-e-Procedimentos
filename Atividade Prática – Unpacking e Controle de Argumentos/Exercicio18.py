# Exercício 18 – Parâmetros somente posicionais com /


# Crie uma função chamada registrar_placar com a seguinte assinatura:

# def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...


# A função deve:

# Possuir uma docstring.
# Utilizar os type hints indicados.
# Retornar uma string contendo o placar da partida.
# Exigir que time_a e time_b sejam passados somente por posição.
# Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.


# Faça uma chamada válida utilizando:

# resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
# print(resultado)


# Depois, tente:

# registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)


# Observe o erro e explique em um comentário qual é a função do / na assinatura.