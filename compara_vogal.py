def compara_vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False


letra = input (str("Digite uma letra: "))
resposta = compara_vogal(letra)
print (resposta)
