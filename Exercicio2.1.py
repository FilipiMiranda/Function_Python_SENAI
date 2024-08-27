nome = str(input("Informe seu Nome: "))
idade = int(input("Informe sua idade: "))

def MenorOuMaior(idade):
    if idade >= 18:
        print("Voce é maior de idade")
    else:
        print("Voce é menor de idade")
       
# id = MenorOuMaior(idade)
print(MenorOuMaior(idade))    
    