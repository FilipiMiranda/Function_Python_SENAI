inicio = int(input("Informe o inicio: "))
fim = int(input("Informe o Fim: "))
passo = int(input("Informe a quantidade de passos: "))

def contador(inicio,fim,passo):
    if passo == 0:
        print("Os passos não pode ser Zero")
        return 
    
if inicio < fim:
    print("Contagem Normal:")
    for i in range(inicio,fim +1, passo):
        print(i)
else:
    print("O inicio precisa ser Menor que o fim")  
    
if inicio > fim:
    print("Contagem Reversa:")
    for i in range(inicio,fim -1, -passo):
        print(i)
else:
    print("O inicio precisa ser Maior que o fim")  
                  
    
print(contador(inicio,fim,passo))