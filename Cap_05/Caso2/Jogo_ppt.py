import random as rd

print("-----------------------------------")
print("   JOGO: PEDRA, PAPEL OU TESOURA   ")
print("-----------------------------------")

def jogar():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    computador = rd.choice(opcoes)
    jogador = input("Escolha Pedra, Papel ou Tesoura:").capitalize()
    
    if jogador not in opcoes:
        print("Opção invalida!")
        return 0
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"): 
        print("Você ganhou!")
    elif jogador == computador:
        print("Empate!")
    else:
        print("Você perdeu!")
    print(f"Computador escolheu: {computador}")
jogar()