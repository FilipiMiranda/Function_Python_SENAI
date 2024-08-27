salario = float(input("Informe seu salario: R$ "))

def Calculo(salario):
    if salario > 5000:
        reajuste = salario * 0.10
    else:
        reajuste = salario * 0.15
    salario_reajuste = salario + reajuste
    return salario_reajuste

salario_reajuste = Calculo(salario)

print(f"Seu Salario atual é R$ {salario}")
print(f"Seu Salario reajustado é R$ {salario_reajuste}")

    
        