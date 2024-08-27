base = float(input("Informe o valor da base: "))
altura = float(input("Informe o valor da altura: "))

def area(base,altura):
    resultado = base * altura / 2
    return resultado

res = area(base,altura)
print(f"A area do tirangulo é {res}")