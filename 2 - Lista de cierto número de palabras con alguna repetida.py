# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 6 - Ejercicio 2 - Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista."""
a=(int(raw_input("¿Cuántas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La lista creada es",li
b=raw_input("Dime que palabra quieres comprobar cuantas veces se ha repetido: ")
c=li.count(b)
print "La palabra",b,"se ha repetido",c,"veces."
