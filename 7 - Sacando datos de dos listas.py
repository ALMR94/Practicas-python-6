# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 6 - Ejercicio 7 - Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista."""
a=(int(raw_input("¿Cuántas palabras tiene la primera lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La primera lista creada es",li

b=(int(raw_input("¿Cuántas palabras tiene la segunda lista? ")))
x=1
li2=[]
for x in range (b):
    print "Dime la palabra",x+1
    c=raw_input()
    x+1
    li2.append(c)
print "La segunda lista es",li2

licom=[]
for i in li:
    if i in li2:
        licom+=[i]
print "Palabras que aparecen en las dos listas:",licom

sololi=[]
for i in li:
    if i not in li2:
        sololi+=[i]
print "Palabras que sólo aparecen en la primera lista:",sololi

sololi2=[]
for i in li2:
    if i not in li:
        sololi2+=[i]
print "Palabras que sólo aparecen en la segunda lista:",sololi2

litodas=licom+sololi+sololi2
print "Todas las palabras incluidas en las listas:",litodas
