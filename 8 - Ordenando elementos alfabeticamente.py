# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 6 - Ejercicio 8 - Escribe un programa que permita crear una lista de palabras y que, a continuaci�n, ordene la lista
por orden alfab�tico."""
a=(int(raw_input("�Cu�ntas palabras tiene la lista? ")))
n=1
li=[]
for n in range (a):
    print "Dime la palabra",n+1
    b=raw_input()
    n+1
    li.append(b)
print "La primera lista creada es",li
liord=sorted(li)
print "La liata ordenada es",liord
