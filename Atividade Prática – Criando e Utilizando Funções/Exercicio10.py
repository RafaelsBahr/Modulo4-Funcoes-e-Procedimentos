# Exercício 10 – Sistema de Aprovação de Empréstimo

# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.

# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.


# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:

# renda mensal;
# valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.

# Use:

# percentual = (parcela / renda) * 100


# A função deve retornar esse percentual.

# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:

# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:

# "Aprovado"
# "Análise manual"
# "Recusado"


# Utilize estas regras:

# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".

# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:

# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.

# Exemplo:

# Parcela: R$ 850.00
# Quantidade: 24

# Total pago: R$ 20400.00

# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:

# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:

# --- Análise do empréstimo ---

# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00

# Resultado: Aprovado

# Essa função não deve retornar nenhuma informação.

# Requisitos
# Todas as funções devem possuir type hints.
# Todas devem possuir docstrings.
# calcular_comprometimento_renda() deve retornar float.
# analisar_emprestimo() deve retornar str.
# calcular_total_pagamento() deve retornar float.
# exibir_resultado() deve retornar None.
# Os cálculos devem acontecer dentro das funções responsáveis por eles.
# Não repita cálculos fora das funções.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.

# Fluxo esperado

# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final


# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.

def calcular_comprometimento_renda(renda: float, parcela: float) -> float:
    """Recebe renda mensal, valor da parcela do empréstimo. Calcula e entrega percentual da renda mensal comprometida pela parcela.
    
    Args:
        renda (float): renda mensal
        parcela (float): valor da parcela do empréstimo
        
    Returns:
        float: percentual da renda mensal comprometido pela parcela
    """
    percentual = (parcela / renda) * 100
    return percentual

def analisar_emprestimo(renda: float, valor_solicitado: float, percentual_comprometido: float) -> str:
    """Recebe renda mensal, valor solicitado, percentual comprometido de renda. Calcula e retorna classificação segundo estas regras:
        Se o comprometimento da renda for maior que 40%, retorne "Recusado".
        Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
        Caso contrário, retorne "Aprovado".
        
    Args:
        renda (float): renda mensal
        valor_solicitado (float): valor solicitado
        percentual_comprometido (float): percentual de comprometimento da renda
    
    Returns:
        str: Classificação do empréstimo
    """
    if percentual_comprometido > 40:
        classificacao = "Recusado"
    elif valor_solicitado > 5 * renda:
        classificacao = "Análise manual"
    else:
        classificacao = "Aprovado"
    return classificacao

def calcular_total_pagamento(valor_parcela: float, qtd_parcelas: int) -> float:
    """Recebe valor da parcela, quantidade de parcelas. Calcula e retorna o valor total que será pago ao final do empréstimo
    
    Args:
        valor_parcela (float): Valor da parcela
        qtd_parcelas (int): quantidade de parcelas
        
    Returns:
        float: Valor total que será pago ao final do empréstimo
    """
    total_pago = valor_parcela * qtd_parcelas
    return total_pago

def exibir_resultado(valor_solicitado: float, percentual_comprometido: float, total_pagamento: float, resultado: str) -> None:
    """Recebe valor solicitado, percentual de comprometimento, total que será pago, resultado da analise. E exibe  resumo.

    Args:
        valor_solicitado (float): valor solicitado
        percentual_comprometido (float): percentual de comprometimento
        total_pagamento (float): Total que será pago
        resultado (str): resultado da análise

    Returns:
        None
    """
    print(f"--- Análise do empréstimo ---\n\nValor solicitado: R$ {valor_solicitado:.2f}\nComprometimento da renda: {percentual_comprometido:.1f}%\nTotal a pagar: R$ {total_pagamento:.2f}\n\nResultado: {resultado}")

renda = 2000
parcela = 500
qtd_parcelas = 30
valor_solicitado = 15000
percentual = calcular_comprometimento_renda(renda, parcela)
analise_emprestimo = analisar_emprestimo(renda, valor_solicitado, percentual)
total_pagamento = calcular_total_pagamento(parcela, qtd_parcelas)
exibir_resultado(valor_solicitado, percentual, total_pagamento, analise_emprestimo)