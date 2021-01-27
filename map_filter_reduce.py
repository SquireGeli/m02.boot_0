from functools import reduce


lista = [1,3, -1,15,9, 18]
listaDobles = map(lambda x: x*2, lista)
'''Con la instruccion map se le hace a cada uno de los elementos de la lista lo que se indica
en la funcion lambda en este caso es el doble con lo que el resultado seria: [2,6,-2,30,18]
pero solo en caso de algoritmos sencillos en la lambda, pue, en otro caso, definiriamos una funcion que
colocariamos en lugar de lambda'''
listaPares = filter(lambda x: x%2 == 0, lista)
'''La instruccion filter se usa para obtener de una lista solo aquello que le concretamos mediante la
funcion lambda (en este caso los divisibles por dos, o sea, los que su resto sea = 0)'''

sumatorio = reduce(lambda x, y : x + y, lista)
'''En este caso de reduce lambda usa dos variables. Reduce reduce a un numero todo el contenido de
una lista'''
sumatorioDobles = reduce(lambda x, y : x + y * 2, lista)
suma100 = reduce(lambda x,y: x + y, range(101))

print(list(listaDobles))
print(list(listaPares))
print(sumatorio)
print(sumatorioDobles)
print(suma100)