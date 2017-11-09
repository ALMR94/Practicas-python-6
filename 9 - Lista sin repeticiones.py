# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 6 - Ejercicio 9 - Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista con las palabras de la primera, pero sin palabras repetidas (el orden de las palabras
en la segunda lista no es importante)."""
a=(int(raw_input("¿Cuántas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La primera lista creada es",li
for i in range(len(li)-1, -1, -1):
    if li[i] in li[:i]:
        del(li[i])
print "La lista sin repeticiones es",li
