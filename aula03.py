import os
os.system("cls")


#Continuação Input com Int e Float
#int() -> Converte para inteiro
#float() -> Converte para n quebrado

#Exemplo 1:
# numero = 10
# numero2= input("digite um numero: ")
# print( "o tipo de numero é, ", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2} = ", soma)

# #Exemplo 2:
# num1= input("digite um numero: ")
# soma= float(num1) + 15
# print("A soma de ", num1 , "+", "15", "=", soma)

# #Exemplo 3:
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite um outro numero: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)


#Exercicios Input com Float e Int() - Logica:

# Atividade 1:

# n1 = float(input("digite um numero: "))
# n2 = float(input("digite um numero: "))
# multi = n1 * n2


# print(f" a multi de {n1} * {n2} = " , multi)

#Atividade 2:

# numero= int(input("digite um numero: " ))
# print(f"sucessor: {numero+1}")
# print(f"antecessor: {numero-1}")


# #Atividade 3:
# num1 = float(input("Qual a sua data de nascimento? "))
# num2 = 2025
# print("Sua idade atual é: ")
# print(num2 - num1)


# #PORCENTAGEM:
# print("25% de 100= ", 0.25 * 100)
# print("4% de 400= ", 0.04 * 400)
# print("99% de 1525= ", 0.99 * 1525)

# #Supondo que um produto custa 150 reais
# #E o caixa deu um desconto de 15%
# exemplo= float(input("digite o preço do produto: "))
# desconto= 0.15 * exemplo
# print("o preço do produto com 15% de desconto é ", exemplo-desconto)


print("-"*10,"MERCADO DO CRICKET","-"*10)

item1= (input("digite o nome do produto: " ))
preço1=float(input("digite o preço do produto: "))
item2= (input("digite o nome de outro produto: " ))
preço2=float(input("digite o preço de outro produto: "))
desconto1= 0.10 * preço1
desconto2= 0.25 * preço2
valorfinal1= round(preço1-desconto1,2)
valorfinal2= round(preço2-desconto2,2)




print("-"*10,"CAIXA","-"*10)
print(f"{item1} custa {preço1} com 10% de desconto= {preço1 - desconto1}")
print(f"{item2} custa {preço2} com 25% de desconto= {preço2 - desconto2}")





print("."*20, "TOTAL","."*20)
total= valorfinal1+valorfinal2
print(f"TOTAL DA COMPRA -> R$: {total}" )




        




