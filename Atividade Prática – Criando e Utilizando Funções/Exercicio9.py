# Exercício 9 – Analisando uma entrega

# Você está desenvolvendo uma pequena parte de um sistema de entregas.

# Crie uma função chamada calcular_tempo_estimado() que receba:

# distância da entrega em quilômetros;
# velocidade média do veículo em km/h.

# A função deve calcular e retornar o tempo estimado da entrega em horas.

# Use: tempo = distancia / velocidade

def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """Recebe distancia em Km e velocidade média em km/h, calcula e retorna o tempo estimado em horas
    
    Args:
        distancia (float): distância da entrega em quilômetros
        velocidade (float): velocidade média do veículo em km/h
        
    Returns:
        float: tempo estimado da entrega em horas
    """
    tempo_estimado = distancia / velocidade
    return tempo_estimado

distancia = 60
velocidade = 60

tempo_estimado = calcular_tempo_estimado(distancia, velocidade)

# Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:

# "Entrega rápida" se o tempo for menor ou igual a 1;
# "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
# "Entrega demorada" se o tempo for maior que 3.

def classificar_entrega(tempo_calculado: float) -> str:
    """Recebe o tempo calculado e classifica entrega como:
        "Entrega rápida" se o tempo for menor ou igual a 1;
        "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
        "Entrega demorada" se o tempo for maior que 3.
        
    Args:
        tempo_calculado (float): Tempo estimado da entrega em horas
        
    Returns:
        str: Classificação do tempo de entrega
    """
    if tempo_calculado <= 1:
        tipo_entrega = "Entrega rápida"
    elif tempo_calculado <= 3:
        tipo_entrega = "Entrega normal"
    else:
        tipo_entrega = "Entrega demorada"

    return tipo_entrega

tipo_entrega = classificar_entrega(tempo_estimado)

# Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
# o tempo estimado;
# a classificação.

# Ela deve exibir algo como:
# Tempo estimado: 2.5 horas
# Classificação: Entrega normal

def exibir_resumo_entrega(tempo_estimado: float, classificacao: str) -> None:
    """Recebe o tempo estimado e classificação para exibir resumo da entrega.
    
    Args:
        tempo_estimado (float): tempo estimado em horas.
        classificacao (str): Classificação do tipo de entrega
        
    Returns:
        None
    """
    print(f"Tempo estimado: {tempo_estimado:.2f} horas\nClassificação: {classificacao}")

exibir_resumo_entrega(tempo_estimado, tipo_entrega)

# Requisitos:
# As três funções devem possuir type hints.
# calcular_tempo_estimado() deve retornar float.
# classificar_entrega() deve retornar str.
# exibir_resumo_entrega() deve retornar None.
# Todas devem possuir docstrings.
# O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
# Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
# Cada função deve possuir apenas uma responsabilidade.
