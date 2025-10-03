# Biblioteca tabulate para fazer as tabelas
from tabulate import tabulate
def AdicionarEstoque():
    produtos = [
        ["Código do produto", "Produto", "Unidade"]
    ]

    while True:
    # Inputs da lista
        Codigo = input("Código do produto: ")
        Produto = input("Nome do Produto: ").capitalize()
        Unidade = input("Unidade do produto Kg, L...: ")

        # Lista de variaveis a serem adicionados
        novoProduto = [Codigo, Produto, Unidade]

        # Adiciona a lista de produtos salvos anteriormente na lista de produtos com append
        produtos.append(novoProduto)

            # Headers="firstrow" define o headers como a primeira coluna, pegando como template a lista produtos
            # Tablefmt="fancy_grid" define o estilo da tabela como fancy
        print(tabulate(produtos, headers="firstrow", tablefmt="fancy_grid"))

        continuar = input("Deseja adicionar outro item (S/N)? ").upper()

        if continuar == "N":
            break
        else:
            continue
