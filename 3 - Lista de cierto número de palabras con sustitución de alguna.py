# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 6 - Ejercicio 3 - Escribe un programa que permita crear una lista de palabras y que, a continuaci�n, pida una
palabra y diga cu�ntas veces aparece esa palabra en la lista."""
a=(int(raw_input("�Cu�ntas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La lista creada es",li
b=raw_input("Dime que palabra quieres sustituir: ")
c=li.index(b)
li.remove(b)
d=raw_input("�Por cu�l palabra? ")
li.insert(c, d)
print "La lista modificada es",li
