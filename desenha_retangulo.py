largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

contador = 1
contador2 = 1

while contador <= altura:
    while contador2 <= largura:
        print ("#", end = "")
        contador2 = contador2 + 1
    contador = contador + 1
    contador2 = 1
    print()
