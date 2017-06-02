i = 0

while i <= 20:
    print(2**i)
    i = i+1

print ("Digite uma sequência de valores terminada por zero.")
soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma+valor
    
print ("A soma dos valores digitados é: ", soma)


tamanho = int(input("Digite o tamanho da sequência de números: "))
produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto*valor
    i = i + 1
        
    
print ("O produto dos valores digitados é: ", produto)
