# 📦 Sistema de Gerenciamento de Estoque em Python

Este é um projeto simples de gerenciamento de estoque, construído em Python, que utiliza a biblioteca **Pandas** para armazenar e manipular dados em um arquivo Excel (`produtosCadastrados.xlsx`) e a biblioteca **Matplotlib** para visualização gráfica do estoque.

## ✍️ Desenvolvedor(es)

* Pedro Henrique Gonçalves Saraiva
* Rafael Vieira Klos 
* Samara Nascimento Santos
* Samuel Wirley Andrade Cruz
  
## 🏫 Contexto Acadêmico

* **Disciplina:** Técnicas de Desenvolvimento de Algoritmos
* **Instituição/Curso:** UDF Centro Universitário / Curso de Análise e Desenvolvimento de Sistemas
* **Professor(a) Orientador(a):** Karla Roberto Sartin
* **Período/Ano:** 2º Período - 2025/2

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto foi aplicar e consolidar conhecimentos técnicos em **Python** para a manipulação e visualização de dados, especificamente:

* **Manipulação de Dados:** Utilização da biblioteca **Pandas** para carregar, processar, e gerenciar dados de estoque.
* **Visualização de Dados:** Emprego da biblioteca **Matplotlib** para gerar gráficos e *insights* visuais a partir dos dados processados.
* **Contexto Prático:** Simular um sistema de **Gerenciamento de Estoque** para demonstrar a aplicação das ferramentas em um cenário de negócios real.



## ✨ Funcionalidades

O sistema é operado via linha de comando e oferece as seguintes funcionalidades principais:

* **Adicionar Produto:** Insere novos itens no estoque ou **atualiza a quantidade** de itens existentes, evitando duplicação por Código ou Nome.
* **Excluir Produto:** Remove itens do estoque usando o Código ou Nome do produto como critério.
* **Emitir Relatório:** Exibe uma tabela consolidada de todos os produtos com a soma total das quantidades.
* **Gerar Gráfico:** Visualiza o estoque total por produto em um gráfico de barras, facilitando a identificação dos itens com maior volume.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem principal do projeto. |
| **Pandas** | Leitura, manipulação e escrita do arquivo Excel (`.xlsx`). |
| **Matplotlib** | Geração do gráfico de barras para visualização do estoque. |
| **Excel** (`.xlsx`) | Base de dados persistente que armazena os registros. |

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para preparar e rodar o sistema na sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o **Python 3** instalado.

### 2. Instalação de Dependências

O projeto requer `pandas` e `matplotlib`. Instale-os usando o `pip`:

```bash
pip install pandas openpyxl matplotlib
