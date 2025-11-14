import pandas as pd # Biblioteca pandas para utilizar excel
import matplotlib.pyplot as plt # Biblioteca matplotlib para gráficos
        
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
        Quantidade = float(input("Digite a quantidade do produto: "))

        novosProdutos = {
            'Código': [Codigo],
            'Produto': [Produto],
            'Categoria': [Categoria],
            'Unidade': [Unidade],
            'Quantidade': [Quantidade]
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

def EmitirRelatorio():
    # Ler o arquivo específico para carregar os dados
    # É fundamental que a coluna 'Quantidade' seja numérica.
    try:
        dfExistente = pd.read_excel('produtosCadastrados.xlsx')
        # Garante que a coluna 'Quantidade' é float para somar corretamente
        dfExistente['Quantidade'] = pd.to_numeric(dfExistente['Quantidade'], errors='coerce')
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo Excel: {e}")
        return
    
    # Exibir o relatório completo dos produtos cadastrados
    print("\nRelatório de Produtos Cadastrados:")
    print(dfExistente.to_string())    

    continuar = input("\nGostaria de visualizar em forma de gráfico (S/N)? ").upper()
    if continuar == 'S':
            
        # Agrupa e soma a Quantidade para cada Produto
        dados_para_grafico = dfExistente.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
            
        # Prepara os Eixos
        infox = dados_para_grafico.index  # Nomes dos produtos (Eixo X)
        infoy = dados_para_grafico.values # Quantidades em estoque (Eixo Y)
            
        plt.figure(figsize=(12, 7))
        plt.bar(infox, infoy, color='teal')
            
        # Customização
        plt.title('Quantidade Total em Estoque por Produto')
        plt.xlabel('Produto', fontsize=12)
        plt.ylabel('Quantidade em Estoque (Unidades)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        
        for i, valor in enumerate(infoy):
            plt.text(i, valor + (max(infoy) * 0.01), f'{valor:.2f}', ha='center', va='bottom')
            
        plt.tight_layout()
        plt.show()
            
    else:
        return
