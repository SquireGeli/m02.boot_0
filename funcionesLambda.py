from funciones1erNivel import sumaTodos
cubo = lambda x: x**3
doble = lambda x: x*2
triple = lambda x: x*3

print(sumaTodos(3, lambda x: x**3))
print(sumaTodos(3, cubo))
'''Las funciones Lambda se pueden usar "a capon" directamente o adjudicarselas a una
variable para darle mas claridad al codigo y porque van a ser puntuales no las reutilizaremos'''
print(sumaTodos(3, doble))
print(sumaTodos(100, triple))