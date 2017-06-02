def fatorial (n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print (fatorial)
    
n = int(input("Digite um número inteiro e positivo: "))
while n >= 0:
    fatorial(n)
    n = int(input("Digite um número inteiro e positivo: "))



