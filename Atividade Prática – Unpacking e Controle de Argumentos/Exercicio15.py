# Exercício 15 – Unpacking com * e valores padrão


# Crie uma função chamada calcular_media com os seguintes parâmetros:

# nota1
# nota2
# nota3
# bonus=0


# A função deve:

# Utilizar type hints em todos os parâmetros e no retorno.
# Possuir uma docstring.
# Calcular a média das três notas.
# Somar o valor de bonus ao resultado final.
# Retornar a média calculada.


# Considere:

# notas = [8.5, 7.0, 9.5]


# Chame a função utilizando * para desempacotar as notas:

# resultado = calcular_media(*notas)
# print(resultado)


# Depois, faça uma segunda chamada utilizando a mesma lista, mas informe bonus como argumento nomeado.



# Por fim, altere a lista para possuir quatro notas:

# notas = [8.5, 7.0, 9.5, 10.0]


# Tente realizar novamente:

# calcular_media(*notas)


# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.