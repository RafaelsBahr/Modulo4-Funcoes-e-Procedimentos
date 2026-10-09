# Exercício 17 – *args recebendo e * desempacotando

# Crie uma função chamada calcular_total_gols que receba uma quantidade variável de números utilizando *args.

def calcular_total_gols(*args: int) -> int:
    """Recebe quantidade variável de gols. Calcula e retorna a soma de gols
    
    Args:
        args (int): Quantidade de gols
        
    Returns:
        (int): Soma de gols
    """
    return sum(args)

# A função deve:

# Utilizar type hint no *args.
# Possuir uma docstring.
# Somar todos os valores recebidos.
# Retornar o total de gols.
# Considere as listas:

primeiro_tempo = [1, 2, 1]
segundo_tempo = [2, 1]

# Chame a função desempacotando as duas listas na mesma chamada:

total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
print(total)

# Depois, escreva comentários no código explicando a diferença entre:

# def calcular_total_gols(*gols):...
# e:

# calcular_total_gols(*primeiro_tempo)

# Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.

# Resposta: def calcular_total_gols(*gols):... -> é uma função que recebe vários argumentos, não se sabe quantos
# calcular_total_gols(*primeiro_tempo) -> é uma chamada da função que desempacota vários argumentos posicionais