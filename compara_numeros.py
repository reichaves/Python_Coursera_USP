def compara_num(a, b):
    if a > b:
        return a
    else:
        return b
        
a = int(input("Digite o primeiro número: "))

b = int(input("Digite o segundo número: "))

maior = compara_num(a,b)
print ("O número maior é", maior)
