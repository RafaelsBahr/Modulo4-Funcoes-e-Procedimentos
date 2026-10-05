# Exercício 10 – Parâmetro normal e *args

# Crie uma função chamada:

# convocar_selecao(pais, *jogadores)

# O primeiro argumento deve representar o país da seleção.

# Todos os argumentos posicionais seguintes devem representar os jogadores convocados.

# Exemplo de chamada:

# convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")

# A função deve mostrar primeiro o país e depois cada jogador convocado.

def convocar_selecao(pais, *jogadores) -> None:
    print(f"Jogadores da seleção {pais}:")
    for jogador in jogadores:
        print(jogador)

convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")