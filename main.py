import function
while True:
        print("\n" + function.TITULO + "=" * 30)
        print(" Sistema de Gerenciamento de Estoque")
        print("=" * 30 + function.RESET)
        print(f"{function.INFO}1 - Adicionar Produto (Estoque)")
        print("2 - Emitir Relatório (e Gráfico)")
        print("3 - Excluir Produto")
        print("0 - Sair" + function.RESET)
        
        escolha = input(f"{function.NEGRITO}Selecione uma opção: {function.RESET}")
        
        if escolha == '1':
            function.AdicionarEstoque()
        elif escolha == '2':
            function.EmitirRelatorio()
        elif escolha == '3':
            function.ExcluirProduto()
        elif escolha == '0':
            print(f"{function.TITULO}Saindo do sistema. Até mais!{function.RESET}")
            break
        else:
            print(f"{function.ERRO}Opção inválida. Tente novamente.{function.RESET}")
