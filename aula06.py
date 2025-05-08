import os
import random 
os.system("cls")

#ESTRUTURAS CONDICIONAIS IF ELSE(ELIF)
#SWITCH CASE -> (Match Case) Escolha o caso (A partir da versão 3.10)
#Match valor:
#Case valor:






# print("1= Segunda ")
# print("2= Terça ")
# print("3= Quarta ")
# print("4= Quinta ")
# print("5= Sexta ")
# print("6= Sabado ")
# print("7= Domingo ")

# semana = int(input("Digite um numero de 1 até 7: "))


# match semana :
#     case 1:
#         print("é segunda")
#     case 2:
#         print("é terça")
#     case 3:
#         print("é quarta")
#     case 4:
#         print("é quinta")
#     case 5:
#         print("é sexta")
#     case 6:
#         print("é sabado")
#     case 7:
#         print("é domingo")




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("-"*20,"LOJA DO SEU ZÉ APARELHOS","-"*20)
# print(" 1= IPHOME  ")
# print(" 2= SAMSUNGA  ")
# print(" 3= XIMONI  ")

# celular = int(input("Digite o numero do celular que voce deseja levar: "))

# match celular :
#     case 1:
#         print("Voce quer levar o Iphome: ")
#         print("O preço dele é de 5.000R$! ")
    
#     case 2:
#         print("Voce quer levar o Samsunga: ")
#         print("O preço dele é de 3.000R$! ")


#     case 3:
#         print("Voce quer levar o Ximoni: ")
#         print("O preço dele é 2.500R$! ")

# print("-"*20,"FRETE","-"*20)

# frete= print(("Existe um frete dependendo da sua região: "))
# print("1=RJ= 10.00")
# print("2=MG= 20.00")
# print("3=SP= 30.00")

# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ATIVIDADE: PEDRA, PAPEL OU TESOURA

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
# #     case _ if valor ==50:
# #         print("= 50")
# #     case _ if valor > 50:
# #         print("maior que 50")




# print("-"*20,"PEDRA OU PAPEL OU TESOURA!","-"*20) LUCAS PRATTI:

# import random

# opções = ["pedra", "papel", "tesoura"]
# escolhadousuario = input("Escolheu pedra, papel, ou tesoura: ")
# escolhadopc = random.choice(opções)

# usuariodopc=0
# maquinamaldita=0
# print("Voce escolheu: ", escolhadousuario)
# print("Computador escoheu: ", escolhadopc)

# if escolhadousuario == escolhadopc:
#     print("Foi um empate!")


# #VOCE GANHOU:

# match usuariodopc:


#     case _ if escolhadousuario == "pedra" and escolhadopc == "tesoura":
#             print("Voce ganhou!")

#     case _ if escolhadousuario == "tesoura" and escolhadopc == "papel":
#             print("Voce ganhou!")

#     case _ if escolhadousuario == "papel" and escolhadopc == "pedra":
#             print("Voce ganhou!")
    
#     case _ if escolhadousuario == "pedra" and escolhadopc == "tesoura":
#             print("Voce ganhou!")



# #PC GANHOU:

# match maquinamaldita:

#     case _ if escolhadousuario == "tesoura" and escolhadopc == "pedra":

#             print("Voce perdeu!")

#     case _ if escolhadousuario == "papel" and escolhadopc == "tesoura":

#             print("Voce perdeu!")

#     case _ if escolhadousuario == "pedra" and escolhadopc == "papel":

#             print("Voce perdeu!")

#     case _ if escolhadousuario == "tesoura" and escolhadopc == "pedra":

#             print("Voce perdeu!") 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CORREÇÃO DA ATIVIDADE:
#LUCAS MOREIRA

print("JOGO PEDRA PAPEL TESOURA")

papel = """
PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador = input("Escolha entre pedra, papel ou tesoura: ")
match jogador:
    case "pedra":
        jogador=pedra
    case "tesoura": 
        jogador =tesoura
    case "papel":
        jogador = papel

#1-> pedra , 2-> papel , 3->tesoura

maquina = random.randint(1,3)

match maquina:
    case 1:
        maquina=pedra
    case 2: 
        maquina =papel
    case 3:
        maquina =tesoura


print(f"Voce escolheu:  {jogador}")
print(f"Maquina escolheu: {maquina}")

match jogador:
    case _ if jogador == maquina:
        print("Empate! ")
    case _ if jogador==pedra and maquina ==tesoura:
        print("Voce ganhou! ")
    case _ if jogador == tesoura and maquina ==papel:
        print("Voce ganhou! ")
    case _ if jogador == papel and maquina ==pedra:
        print("Voce ganhou! ")
    case _ :
        print("Voce perdeu! ")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#DANIEL:
print("2 MODO - PEDRA PAPEL TESOURA")


print("JOGO PEDRA PAPEL TESOURA ")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#pedra=1 papel=2 tesoura=3
mao = input("Digite pedra ou papel ou tesoura :")
maquina = random.randint(1,3)

match maquina :
    case 1:
        maquina = "pedra"
    case 2:
        maquina = "papel"
    case 3 :
        maquina ="tesoura"

match mao:

    case _ if mao== "pedra" and maquina=="pedra" :
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {pedra}")
        print("EMPATOU!")
    
    case _ if mao== "pedra" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {pedra}")
        print("PERDEU!")
    case _ if mao== "pedra" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {pedra}")
        print("GANHOU!")
    case _ if mao== "papel" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {papel}")
        print("EMPATOU!")
    case _ if mao== "papel" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {papel}")
        print("GANHOU")
    case _ if mao== "papel" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {papel}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {tesoura}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {tesoura}")
        print("GANHOU!")
    case _ if mao== "tesoura" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {tesoura}")
        print("EMPATOU!")
    case _:
        print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       