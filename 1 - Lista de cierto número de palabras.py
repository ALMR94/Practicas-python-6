# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 6 - Ejercicio 1 - Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un n�mero y luego solicitar ese n�mero de palabras para crear la lista. Por �ltimo, el
programa tiene que escribir la lista."""
a=(int(raw_input("�Cu�ntas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La lista creada es",li
