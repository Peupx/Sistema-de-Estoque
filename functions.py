import pandas as pd
import matplotlib.pyplot as plt

# Definição das Cores ANSI como Variáveis Globais
# Permite colorir o terminal para notificações
RESET = '\033[0m'
SUCESSO = '\033[92m'  # Verde
ERRO = '\033[91m'    # Vermelho
AVISO = '\033[93m'    # Amarelo
INFO = '\033[94m'     # Azul
TITULO = '\033[95m'   # Magenta
NEGRITO = '\033[1m'

# Funções do Sistema

def AdicionarEstoque():
    # Carrega o arquivo ou cria um DataFrame novo se não existir.
    try:
        dfExistente = pd.read_excel('produtosCadastrados.xlsx')
        dfExistente['Quantidade'] = pd.to_numeric(dfExistente['Quantidade'], errors='coerce')
    except FileNotFoundError:
        print(f"{AVISO}Arquivo não encontrado. Criando um novo DataFrame.{RESET}")
        dfExistente = pd.DataFrame(columns=['Código', 'Produto', 'Categoria', 'Unidade', 'Quantidade'])
    except Exception as e:
        print(f"{ERRO}Erro ao ler o Excel: {e}{RESET}")
        return

    while True:
        print(f"\n{TITULO}--- Adicionar Novo Produto ---{RESET}")
        
        # Coleta de dados do produto.
        Codigo = input(f"Digite o código do produto: ")
        Produto = input(f"Digite o nome do produto: ")
        Categoria = input(f"Digite a categoria do produto: ")
        Unidade = input(f"Digite a unidade do produto Ex: Kg, L... : ")
        
        try:
            Quantidade = float(input(f"Digite a quantidade do produto: "))
        except ValueError:
            print(f"{ERRO}Erro: A quantidade deve ser um número.{RESET}")
            continue
        
        # Verifica se o produto já existe pelo Código OU Nome para evitar duplicatas.
        mascara_codigo = dfExistente['Código'].astype(str) == Codigo
        mascara_nome = dfExistente['Produto'].astype(str).str.upper() == Produto.upper()
        produto_existente = dfExistente[mascara_codigo | mascara_nome]
        
        # Lógica de Duplicação: Se encontrado, pergunta se deve somar a quantidade.
        if not produto_existente.empty:
            idx_existente = produto_existente.index[0]
            nome_existente = dfExistente.loc[idx_existente, 'Produto']
            
            print(f"\n{AVISO}{NEGRITO}Aviso: Item existente!{RESET}{AVISO}")
            print(f"Item '{nome_existente}' (Código: {dfExistente.loc[idx_existente, 'Código']}) já está no estoque.{RESET}")
            
            adicionar_ao_existente = input(f"{INFO}Adicionar {Quantidade} ao estoque existente (S/N)? {RESET}").upper()
            
            if adicionar_ao_existente == 'S':
                # Atualiza a linha existente.
                quantidade_antiga = dfExistente.loc[idx_existente, 'Quantidade']
                dfExistente.loc[idx_existente, 'Quantidade'] += Quantidade
                dfExistente.loc[idx_existente, 'Categoria'] = Categoria
                dfExistente.loc[idx_existente, 'Unidade'] = Unidade
                
                print(f"{SUCESSO}Estoque de '{nome_existente}' atualizado de {quantidade_antiga:.2f} para {dfExistente.loc[idx_existente, 'Quantidade']:.2f}.{RESET}")
            else:
                print(f"{AVISO}Produto não adicionado. Prosseguindo...{RESET}")
        
        # Adiciona como novo item, se não existir.
        else:
            novosProdutos = {
                'Código': [Codigo],
                'Produto': [Produto],
                'Categoria': [Categoria],
                'Unidade': [Unidade],
                'Quantidade': [Quantidade]
            }
            dfNovo = pd.DataFrame(novosProdutos)
            dfExistente = pd.concat([dfExistente, dfNovo], ignore_index=True)
            print(f"{SUCESSO}Novo produto adicionado.{RESET}")
        
        # Salva as alterações no arquivo Excel.
        try:
            dfExistente.to_excel('produtosCadastrados.xlsx', index=False)
            print(f"{INFO}Arquivo salvo!{RESET}")
        except Exception as e:
            print(f"{ERRO}Erro ao salvar no Excel: {e}{RESET}")
            break

        # Opção de sair do loop.
        continuar = input("\nContinuar adicionando produtos (S/N)? ").upper()
        if continuar == 'N':
            break

def ExcluirProduto():
    
    # Tenta carregar o arquivo.
    try:
        dfExistente = pd.read_excel('produtosCadastrados.xlsx')
    except FileNotFoundError:
        print(f"{ERRO}Erro: Arquivo não encontrado. Nada para excluir.{RESET}")
        return
    except Exception as e:
        print(f"{ERRO}Erro ao ler o Excel: {e}{RESET}")
        return

    print(f"\n{TITULO}Excluir Produto do Estoque{RESET}")
    
    if dfExistente.empty:
        print(f"{AVISO}Estoque vazio. Nada para excluir.{RESET}")
        return

    # Exibe itens para facilitar a escolha.
    print(f"\n{INFO}Produtos Atuais:{RESET}")
    print(dfExistente[['Código', 'Produto']].to_string(index=False))
    print("-" * 30)

    # Escolhe o critério de exclusão (Código ou Nome).
    criterio = input("Excluir por Código ou Nome? (C = Código / N = Nome)").upper()
    
    if criterio == 'C':
        coluna = 'Código'
        valor_excluir = input(f"Digite o Código: ")
    elif criterio == 'N':
        coluna = 'Produto'
        valor_excluir = input(f"Digite o Nome: ")
    else:
        print(f"{AVISO}Opção inválida.{RESET}")
        return

    # Cria máscara de exclusão e verifica se o item existe.
    mascara = dfExistente[coluna].astype(str) == valor_excluir
    num_excluidos = mascara.sum()
    
    if num_excluidos == 0:
        print(f"{AVISO}Nenhum produto encontrado com {coluna}: '{valor_excluir}'.{RESET}")
        return

    # Remove as linhas (o ~ inverte a máscara: mantém o que NÃO corresponde).
    dfAtualizado = dfExistente[~mascara].copy()

    # Salva o DataFrame atualizado.
    try:
        dfAtualizado.to_excel('produtosCadastrados.xlsx', index=False)
        print(f"\n{SUCESSO}{NEGRITO}Sucesso!{RESET}{SUCESSO} {num_excluidos} item(ns) excluído(s) e arquivo salvo.{RESET}")
    except Exception as e:
        print(f"{ERRO}Erro ao salvar alterações no Excel: {e}{RESET}")

def EmitirRelatorio():
    # Tenta carregar o arquivo e garante o tipo numérico.
    try:
        dfExistente = pd.read_excel('produtosCadastrados.xlsx')
        dfExistente['Quantidade'] = pd.to_numeric(dfExistente['Quantidade'], errors='coerce')
    except FileNotFoundError:
        print(f"{ERRO}Erro: O arquivo não foi encontrado.{RESET}")
        return
    except Exception as e:
        print(f"{ERRO}Erro ao ler o Excel: {e}{RESET}")
        return
    
    print(f"\n{TITULO}Relatório de Produtos Cadastrados (Consolidado){RESET}")
    
    if dfExistente.empty:
        print(f"{AVISO}A planilha de estoque está vazia.{RESET}")
        return
        
    # Agrupa e consolida para o relatório (soma quantidades por produto).
    dfRelatorio = dfExistente.groupby(['Código', 'Produto', 'Categoria', 'Unidade'])['Quantidade'].sum().reset_index()

    # Exibe a tabela.
    print(f"{INFO}{dfRelatorio.to_string()}{RESET}")

    continuar = input("\nGostaria de visualizar em forma de gráfico (S/N)? ").upper()
    if continuar == 'S':
        dados_para_grafico = dfRelatorio.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
        
        if dados_para_grafico.empty:
            print(f"{AVISO}Não há dados de quantidade para o gráfico.{RESET}")
            return
        
        # Prepara e exibe o gráfico de barras.
        infox = dados_para_grafico.index
        infoy = dados_para_grafico.values
        
        plt.figure(figsize=(12, 7))
        plt.bar(infox, infoy, color='teal')
        
        plt.title('Quantidade Total em Estoque por Produto')
        plt.xlabel('Produto', fontsize=12)
        plt.ylabel('Quantidade em Estoque (Unidades)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        
        for i, valor in enumerate(infoy):
            plt.text(i, valor + (max(infoy) * 0.01), f'{valor:.2f}', ha='center', va='bottom')
            
        plt.tight_layout()
        plt.show()
