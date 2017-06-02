num = int (input("Digite um número inteiro: "))
n = 2
# Resto da divisão por 10 sempre devolve último dígito
# Fazer a divisão inteira joga fora o último dígito

sequencia = True


while num != 2 and num!= 1 and num > n:
    if num % n == 0 and num != n:
        sequencia = False
            
    n = n + 1

if sequencia and not num == 1:
    print ("primo")
else:
    print ("não primo")
