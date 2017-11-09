# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 6 - Ejercicio 1 - Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
programa tiene que escribir la lista."""
a=(int(raw_input("¿Cuántas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La lista creada es",li
