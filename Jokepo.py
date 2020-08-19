import random
#print(random.randint(10,50))

while True:

    pergunta1 = int(input("""Com quem deseja jogar: 

    1 - Computador
    2 - Outro jogador
    3 - Sair
    
    Digite o numero que escolhido: """))

    if pergunta1 == 1:
        pergunta2 = int(input("""Escolha opcao:

        1 - Pedra
        2 - Papel
        3 - Tesoura
        
        Digite o numero escolhido: """))

        computador = random.randint(1,3)
        if computador == 1:
            print("o computador jogou pedra")
        if computador == 2:
            print("o computador jogou papel")
        if computador == 3:
            print("o computador jogou tesoura")        

        if pergunta2 == computador:
            print("Empate")
        elif pergunta2 == 1 and computador == 2: #Pedra contra papel
            print("Jogador 1 ganhou!")
        elif pergunta2 == 2 and computador == 1: #Papel contra pedra
            print("computador ganhou!")
        elif pergunta2 == 2 and computador == 3: #Papel contra tesoura
            print("computador ganhou!")
        elif pergunta2 == 3 and computador == 2: #Tesoura contra papel
            print("Jogador ganhou!")
        elif pergunta2 == 1 and computador == 3: #Pedra contra tesoura
            print("Jogador ganhou!")
        elif pergunta2 == 3 and computador == 1: #Tesoura contra pedra
            print("computador ganhou!")

    elif pergunta1 == 2:
        jogador1 = int(input("""Escolha opcao:

        1 - Pedra
        2 - Papel
        3 - Tesoura
        
        Digite o numero escolhido: """))

        jogador2 = int(input("""Escolha opcao:

        1 - Pedra
        2 - Papel
        3 - Tesoura
        
        Digite o numero escolhido: """))

        if jogador1 == jogador2:
            print("Empate")
        elif jogador1 == 1 and jogador2 == 2: #Pedra contra papel
            print("Jogador1 ganhou!")
        elif jogador1  == 2 and jogador2 == 1: #Papel contra pedra
            print("Jogador2 ganhou!")
        elif jogador1  == 2 and jogador2 == 3: #Papel contra tesoura
            print("Jogador2 ganhou!")
        elif jogador1  == 3 and jogador2 == 2: #Tesoura contra papel
            print("Jogador1 ganhou!")
        elif jogador1  == 1 and jogador2 == 3: #Pedra contra tesoura
            print("Jogador1 ganhou!")
        elif jogador1  == 3 and jogador2 == 1: #Tesoura contra pedra
            print("Jogador2 ganhou!")    


    elif pergunta1 == 3:
        print("Adios!")
        break
    else: 
        print("Opcao invalida!!!!!!!!!!!!!!!!1")
        


