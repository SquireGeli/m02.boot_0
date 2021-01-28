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
        
def ladrar():
    print("No tengo perro")
    
Maig = Perro("Maig",8,40)
Max = Perro("Max",5,4)
print(Maig, "y ladro asi:")
Maig.ladrar()
print(Max, "y ladro asi:")
Max.ladrar()
