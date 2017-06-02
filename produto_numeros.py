tamanho = int (input("Quantos números você quer digitar? "))

produto = 1
i= 0

while i < tamanho:
    valor = int (input("Digite um valor para multiplicar: "))
    produto = produto * valor
    i = i + 1

print ("O produto dos números é ", produto)
