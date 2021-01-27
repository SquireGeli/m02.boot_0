'''La recursividad es una funcion que para repetirse se invoca a si misma'''
def retrocontador (e):
    print ("{},". format(e), end="")
    if e == 0:
        return
    retrocontador (e -1)
    
retrocontador(10)
'''Si no se le indica que termine en el 0, el programa entraria en un bucle infinito hasta bloquearnos.
El segundo punto importante de la recursividad es que siempre haya un punto de parada, donde termine de
autollamarse a si misma'''

def sumatorio(m):
    if m != 0:
        return m + sumatorio(m-1)
    else:
        return 0