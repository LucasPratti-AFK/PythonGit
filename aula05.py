import os 
os.system("cls")
# #IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
# #ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# # ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
# #  SE MENOR QUE 12 -> CRIANÇA
# #  SE MENOR QUE 18 -> ADOLESCENTE
# #  SE MENOR QUE 60 -> ADULTO
# #  SE NAO -> IDOSO


# # NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES:
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA:
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")






# ATIVIDADE 1: NOTAS
# replace("valor1","valor2")-> Substitui o valor1 pelo valor2

# nota1= float(input("digite sua nota: "))
# nota2= float(input("digite sua nota: "))
# media= (nota1+nota2)/2
# print(media)

# if media <= 5 :
#     print("Reprovado")
# elif media >= 5 and media <=7 :
#     print("Recuperação")

# elif media >= 7 :
#     print("Aprovado")

# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)


#PROGRAMA DE MASSA CORPÓREO:

# peso= float(input("digite seu peso: "))

# altura= float(input("digite sua altura: "))

# imc= peso/(altura * altura)

# print(f"Seu imc : {imc}")

# if imc < 17 :
#     print("muito abaixo do peso")

# elif imc >=17 and imc <= 18.49 :
#     print("peso normal")

# elif imc >= 18.5 and imc <= 24.99:
#     print("acima do peso")

# elif imc >= 30 and imc <= 34.99:
#     print("Obesidade 1")

# elif imc >= 35 and imc <= 39.99:
#     print("Obesidade 2")

# else:
#     print("Obesidade 3")
     

     

print("-"*20,"AUTOCAR","-"*20)

salario= float(input("Digite seu salario: "))
if salario <= 2799.99 :
    print("Seu salario atual é:", salario)
    print("Seu aumento é de: 20%")
    
    aumento= salario * 0.20
    print("Seu aumento é de: " , aumento)
    atual= aumento + salario
    print("Seu novo salario após o aumento é de:" , atual)

elif salario <= 2800.99 and salario < 6999.99 :
    print("Seu salario atual é:", salario)
    print("Seu aumento é de: 15%")
    
    aumento= salario * 1.15
    print("Seu aumento é de: " , aumento)
    atual= aumento + salario
    print("Seu novo salario após o aumento é de:" , atual)

elif salario <= 7000.00 and salario < 14999.99 :
    print("Seu salario atual é:", salario)
    print("Seu aumento é de: 10%")
    
    aumento= salario * 1.10
    print("Seu aumento é de: " , aumento)
    atual= aumento + salario
    print("Seu novo salario após o aumento é de:" , atual)


elif salario <= 15000.00 :
    print("Seu salario atual é:", salario)
    print("Seu aumento é de: 5%")
    
    aumento= salario * 1.05
    print("Seu aumento é de: " , aumento)
    atual= aumento + salario
    print("Seu novo salario após o aumento é de:" , atual)

