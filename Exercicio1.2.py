num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
num3 = float(input("Digite outro numero: "))

def maior(num1,num2,num3):
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    return maior

def menor(num1,num2,num3):
    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor= num3
    return menor

resMaior = maior(num1,num2,num3)
print(f"Maior numero é: {resMaior}")
resMenor = menor(num1,num2,num3)
print(f"Menor numero é: {resMenor}")
    