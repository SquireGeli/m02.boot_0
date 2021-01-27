import random

letras = "ABCDEFGHIJKLMNÑOPQRSTUWXYZ"

class Rotor ():
    letras = 
    def __init__ (self,abecedario="ABCDEFGHIJKLMNÑOPQRSTUWXYZ"):
        self.abecedario = letras
        self.rotor=[]
        otrasLetras = list(self.abecedario)
        for l in self.abecedario :
            n = random.randrange(len(letras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)
        self.rotorC = self.rotor[:]
       
def codifica(self,letra):
    for t in self.rotor:
        if letra == t[0]
            return t[1]

    raise ValueError("{} no pertenece al abecedario".format(letra))

def posicionInicial(self, letra):
    position = self.abecedario.index(letra)
    self.rotorC = self.rotor[position:] + self.rotor[:position]

def avanza(self):
    self.rotorC = self.rotorC[1:] + self-rotorC[0]






