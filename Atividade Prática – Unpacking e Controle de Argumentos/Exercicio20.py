# Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos

# Crie uma função chamada registrar_jogo com a seguinte assinatura:

# def registrar_jogo(
# mandante: str,visitante: str,
# /,
# competicao: str,
# *eventos: str,
# estadio: str,
# encerrado: bool = True,
# **informacoes
# ) -> dict:

# A função deve possuir uma docstring completa explicando:

# O objetivo da função.
# O que cada parâmetro representa.
# O que a função retorna.


# A função também deve seguir estas regras:

# mandante e visitante devem ser informados somente por posição.
# competicao pode ser passada por posição ou pelo nome.
# *eventos deve receber uma quantidade variável de eventos da partida.
# estadio deve obrigatoriamente ser informado pelo nome.
# encerrado deve possuir True como valor padrão.
# **informacoes deve receber informações adicionais da partida.


# Dentro da função, crie e retorne um dicionário contendo:

# Mandante.
# Visitante.
# Competição.
# Eventos.
# Estádio.
# Situação da partida.
# Informações adicionais.
# Teste a função com:

# partida = registrar_jogo(
# "Brasil",
# "Argentina",
# "Copa do Mundo",
# "Gol do Brasil",
# "Cartão amarelo",
# "Substituição",
# estadio="Maracanã",
# publico=70000,
# transmissao="TV"
# )
# print(partida)


# Depois, considere os seguintes dados:

# times = ["França", "Espanha"]
# dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}


# Faça uma segunda chamada utilizando:

# *times para desempacotar os dois primeiros argumentos.
# Uma competição informada normalmente.
# Dois ou mais eventos posicionais.
# **dados para desempacotar as informações nomeadas.


# Ao final, escreva comentários identificando o papel de cada elemento da assinatura:

# /
# *eventos
# estadio
# encerrado=True
# **informacoes


# Explique também a diferença entre:

# *eventos
# na definição da função e:

# *times
# na chamada, assim como a diferença entre:

# **informacoes
# na definição e:

# **dados
# na chamada.

def registrar_jogo(
    mandante: str, 
    visitante: str,
    /, # Todos argumentos antes da barra devem ser posicionais
    competicao: str,
    *eventos: str, # Tupla de argumentos posicionais
    estadio: str, # Depois de uma lista de argumentos posicionais, próximo deve ser obrigatório e um argumento nominal
    encerrado: bool = True, # Argumento nominal e opicional com valor padrão True
    **informacoes: str | int # Dicionário com argumentos nominais, qualquer par nome=valor
    ) -> dict:
    """Recebe informações da partida, reune e retorna tudo num dicionário.
    
    Args:
        mandante (str): Nome do time mandante.
        visitante (str): Nome do time visitante.
        competicao (str): Nome da competição/campeonato.
        *eventos (str): Eventos que ocorreram durante o jogo
        estadio (str): Nome do estadio
        encerrado (bool): Informa se partida foi encerrada. Padrão é encerrado.
        **informacoes (str | int): Outras informações da partida.
        
    Returns:
        (dict): Dicionário com todas informações da partida.
    """
    return {"Mandante": mandante, 
                  "Visitante": visitante, 
                  "Competição": competicao,
                  "Eventos": eventos,
                  "Estádio": estadio,
                  "Encerrado": encerrado,
                  "Informações": informacoes
                  }

partida = registrar_jogo(
    "Brasil",
    "Argentina",
    "Copa do Mundo",
    "Gol do Brasil",
    "Cartão amarelo",
    "Substituição",
    estadio="Maracanã",
    publico=70000,
    transmissao="TV"
    )
print(partida)

times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}

partida = registrar_jogo(*times, "Copa do Mundo", "Cartão amarelo", "Cartão vermelho", **dados)
print(partida)


# Explique também a diferença entre:

# *eventos
# na definição da função e: Este argumento permite receber vários argumentos posicionais

# *times
# na chamada, assim como a diferença entre: Desempacota varios argumentos posicionais

# **informacoes
# na definição e: Este argumento permite receber vários argumentos nomeados

# **dados
# na chamada: Desempacota varios argumentos nomeados