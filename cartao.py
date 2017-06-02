meucartao = int(input("Digite o número do seu cartão de crédito: "))

cartaolido = 1
encontreimeu = False

while cartaolido != 0 and not encontreimeu:
    cartaolido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaolido == meucartao:
        encontreimeu = True

if encontreimeu:
    print ("Eba!")
else:
    print ("Saco!")
