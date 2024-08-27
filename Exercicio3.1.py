num1 = float(input("Digite uma nota: "))
num2 = float(input("Digite outra nota: "))
num3 = float(input("Digite outra nota: "))
    
try:
    
   
    def soma(num1,num2,num3):
        resultado = float (num1 + num2 + num3) / 3
        
        if (num1 < 0 or num2 < 0 or num3 < 0):
            print("Digite uma nota positiva!!") 
      
        return resultado
        
    res = soma(num1,num2,num3)
    print(res)
    
except:
    print("Digite um nota!!!")