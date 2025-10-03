import pandas as pd # Biblioteca pandas para utilizar excel
        
def AdicionarEstoque():
    # Ler o arquivo específico para carregar os dados
    dfExistente = pd.read_excel('produtosCadastrados.xlsx')
    
    # Loop principal para adicionar produtos
    while True:
        
        # Input feito pelo usuário da descrição dos produtos
        Codigo = input("Digite o código do produto: ")
        Produto = input("Digite o nome do produto: ")
        Categoria = input("Digite a categoria do produto: ")
        Unidade = input("Digite a unidade do produto Ex: Kg, L... : ")

        novosProdutos = {
            'Código': [Codigo],
            'Produto': [Produto],
            'Categoria': [Categoria],
            'Unidade': [Unidade]
        }
        # Salva os produtos em um DataFrame novo pegando os novosProdutos como input
        # Além de concatenar eles junto com o DataFrame já existente
        dfNovo = pd.DataFrame(novosProdutos)
        dfExistente = pd.concat([dfExistente, dfNovo], ignore_index=True)

        # Aqui o código tenta salvar as alterações, avisando se ocorreu um erro ou deu tudo certo
        try:
            dfExistente.to_excel('produtosCadastrados.xlsx', index=False)
            print("Produto adicionado e arquivo salvo com sucesso!")
        except:
            print("Ocorreu um erro ao salvar no Excel")
            break 

        # Lugar de quit do programa
        continuar = input("\nContinuar adicionando produtos (S/N)? ").upper()
        if continuar == 'N':
            break
