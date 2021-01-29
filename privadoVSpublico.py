class Timido():
    def __init__(self,nombre):
        self.__nombre = nombre
        
    def preguntarnombreconcuidado (self):
        return self.__nombre
    
chico= Timido("Raul")
if chico.preguntarnombreconcuidado() != None:
    print("{} es un nombre publico". format(chico.preguntarnombreconcuidado()))
else:
    print("Nombre Privado")