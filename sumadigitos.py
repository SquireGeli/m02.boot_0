num = int(input("Introduce un numero: "))
array= []
array.append(num)

for numero in array:
    suma=0
    for digito in str(numero):
        suma += int(digito)
    print("La suma de los digitos de: ", num, " =", suma)
    
base=3
def multiplo (valor, base):
    if valor % base == 0:
        return True
    else:
        print ("La suma de los digitos de: ",num,"no es divisible x ", base)

if multiplo (suma,base):
    total= suma/base
    print(suma,"es divisible x ", base, "=", total)
    print("Asi:", num, "es divisible x ", base, "=", num/base)



