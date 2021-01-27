
año= input("Entra el año: ")
def bisiesto(año):
    
    if int(año) % 4 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
    return año

bisiesto(año)