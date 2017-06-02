num = int (input("Digite um número: "))

# Resto da divisão por 10 sempre devolve último dígito
# Fazer a divisão inteira joga fora o último dígito

sequencia = False

while num != 0:
    ult = num % 10
    num = num // 10
    if num != 0:
        comparault = num % 10
        if ult == comparault:
            sequencia = True
        

if sequencia:
    print ("sim")
else:
    print ("não")
