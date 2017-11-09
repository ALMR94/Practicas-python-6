# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 6 - Ejercicio 5 - Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista."""
a=(int(raw_input("¿Cuántas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La lista creada es",li
b=(int(raw_input("¿Cuántas palabras tiene la segunda lista de palabras eliminatorias? ")))
x=1
li2=[]
for x in range (b):
    print "Dime la palabra",x+1
    c=raw_input()
    d=li.index(c)
    li.remove(c)
    li2.append(c)
    x+1   
print "La segunda lista de palabras eliminatorias es",li2
print "La lista final de palabras es",li

