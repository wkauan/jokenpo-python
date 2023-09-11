from random import choice

opcoes = ["pedra", "papel", "tesoura"]

def escolha_usuario():
    escolha = input("Escolha papel, pedra ou tesoura: ")
    return escolha.lower()

def escolha_computador():
    escolhaComputador = choice(opcoes)

    escolhaUsuario = escolha_usuario()

    if escolhaComputador == escolhaUsuario:
        print("Empate!")
    elif escolhaComputador == "pedra" and escolhaUsuario == "papel" or escolhaComputador == "papel" and escolhaUsuario == "tesoura":
        print("Você venceu! A escolha do computador foi: ", escolhaComputador)
    else:
        print("Você perdeu! A escolha do computador foi: ", escolhaComputador)
        
escolha_computador()
