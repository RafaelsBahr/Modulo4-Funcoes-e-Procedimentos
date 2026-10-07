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

def calcular_media(nota1: float, nota2: float, nota3: float, bonus: float = 0) -> float:
    """
    recebe valores, calcula e retorna a media deles com mais um valor bonus.

    Args:
        nota1 (float): primeiro valor
        nota2 (float): segundo valor
        nota3 (float): terceiro valor
        bonus (float): valor bonus somado a média dos 3

    Returns:
        (float): média dos valores + bonus
    """
    return ((nota1 + nota2 + nota3) / 3) + bonus

notas = [8.5, 7.0, 9.5]

resultado = calcular_media(*notas)
print(f"{resultado:.2f}")

resultado = calcular_media(*notas, bonus=8)
print(f"{resultado:.2f}")

notas = [8.5, 7.0, 9.5, 10.0]
print(f"{calcular_media(*notas):.2f}")

# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.
# Porque nossa função tem espaço apenas para 3 notas, o quarto valor ocupa o espaço do valor bonus porque são argumentos sequenciais