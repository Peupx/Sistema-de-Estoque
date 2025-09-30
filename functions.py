def adicionarEstoque():
    continuar = 1 # Variável condicional do looping
    produtos = {} # Dicionário vazio... até então
    
    while continuar == 1:
        nome = input("Coloque o nome do produto: ").capitalize()
        # Pega o input se já não esiver no dicionário
        if nome in produtos:
            print("Inválido! Nome já consta na lista")
        else:
            quantidade = input("Coloque a quantidade desse produto: ")
            produtos[nome] = quantidade
            
            
        print(produtos)
        
        continuar = input("Deseja continuar? (S/N)").upper()
        # Alteração da condicional de lopping de acordo com o input anterior
        if continuar == 'N': 
            continuar = 0
            
        elif continuar == 'S':
            continuar = 1
