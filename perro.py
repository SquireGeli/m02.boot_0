class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def ladrar(self):
        if self.peso >= 8:
            print ("GUAU,GUAU")
        else:
            print ("Guau,guau")
    def __str__(self):
         return "Soy el perro: {},tengo: {} años, y peso: {}kg"\
              .format(self.nombre,self.edad,self.peso)
class Perroasistencia(Perro):
    def __init__(self, nombre,edad,peso, amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
    def __str__(self):
         return "Soy el perro de asistencia: {},tengo: {} años, y peso: {}kg y mi dueño es: {}"\
              .format(self.nombre,self.edad,self.peso,self.amo)
    def pasear(self):
        print("Y yo {} que soy perro de asistencia, ayudo a mi dueño {} a pasear".format(self.nombre,self.amo))

    def ladrar(self):
        if self.__trabajando:
            print("No puedo ladrar porque estoy trabajando")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando= valor
        

def ladrar():
    print("No tengo perro")
    
Maig = Perro("Maig",8,40)
Max = Perro("Max",5,4)
Bjorn = Perroasistencia ("Bjorn",5,30,"Kat")
print(Maig, "y ladro asi:")
Maig.ladrar()
print(Max, "y ladro asi:")
Max.ladrar()
print(Bjorn, "y ladro asi:")
Bjorn.trabajando = True
Bjorn.ladrar()
Bjorn.pasear()