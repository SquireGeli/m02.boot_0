print ("SI AL REFLEJO DE UN NUMERO CUALQUIERA LE RESTAS DICHO NUMERO")
print ("Y DICHA DIFERENCIA ES DIFERENTE DE O (PORQUE AMBOS SON IGUALES)")
print ("DA SIEMPRE UN NUMERO ENTERO DIVISIBLE POR 3. HAZ LA PRUEBA")

numero= input ("Introduce un numero: ")
isvalid = False
def specul (numero):
    reverse=""
    for digit in numero:
        reverse= digit + reverse
    return reverse

while not isvalid:
    if numero == specul(numero):
        print (int(specul(numero)), " - " ,int(numero), "= ", int(specul(numero)) - int(numero))
        numero= input ("Introduce otro numero, ese no es valido: ")
    else:
        total = int(specul(numero)) - int(numero)
        print (int(specul(numero)), " - " ,int(numero), "= ", total)
        print (total,"/3 = ", total/3)
        isvalid= True
        

