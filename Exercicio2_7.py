import math

a = int(input ("Digite a coordenada x do primeiro ponto: "))
b = int(input ("Digite a coordenada y do primeiro ponto: "))
c = int(input ("Digite a coordenada x do segundo ponto: "))
d = int(input ("Digite a coordenada y do segundo ponto: "))

numero = ((a-c)**2) + ((b-d)**2)

dist = math.sqrt(numero)

if dist >= 10:
    print ("longe")
else:
    print ("perto")
