# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 6 - Ejercicio 10 - Escribe un programa que pida un n�mero y a continuaci�n escriba la lista de todos los divisores
del n�mero (incluidos el uno y �l mismo)."""
n = int(input("Escribe un n�mero: "))
num=n
div = 0
li=[]
print("Divisores:")
if n % 2 == 0:
    iterar = n / 2
else:
    iterar = (n - 1) / 2

for i in range(1, int(iterar) + 1):
    if n % i == 0:
        aux = n / i
        if aux != div:
            div = aux
        if i == iterar:
            li.append(div)
        else:
            li.append("%d" % div)
li.append(num/num)
numli=len(li)
print "El n�mero",num,"tiene",numli,"divisores:",li
