def soma(a, b):
    return a + b

def multiplicação(a, b ):
    return a * b 

def divisão (a, b):
    if b == 0:
        return"Erro: Divisão por zero!"
    return a / b

def subtração (a, b):
    return a - b



print("==== CALCULADORA ====")
print("1 - SOMA")
print("2 - MULTIPLICAÇÃO")
print("3 - DIVISÃO")
print("4 - SUBTRAÇÃO")

operação = input("Escolha uma operação: ")


num1 = float(input("Digite um número:")) 
num2 = float(input("Digite um número:")) 

if operação == "1":
    print("Resultado :", soma(num1, num2))
elif operação == "2":
    print("Resultado:", multiplicação(num1, num2))
elif operação == "3":
     print("Resultado:", divisão(num1, num2))
elif operação == "4":
     print("Resultado:", subtração(num1, num2))
else:
    print("Opção Inválida!")





