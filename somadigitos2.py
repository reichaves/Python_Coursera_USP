num = int (input("Digite um número inteiro: "))
soma = 0

# Resto da divisão por 10 sempre devolve último dígito
# Fazer a divisão inteira joga fora o último dígito


while num != 0:
    ult = num % 10
    soma = soma + ult
    num = num // 10
            
print (soma)
