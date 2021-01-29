'''conversor privadoo'''
class Termometro():
    def __init__(self):
        self.__umedida = 'C'
        self.__temperatura = 0
        '''Los guioncitos por delante los hacen privados,aunque solamente los simula'''
    def __conversor(self,temperatura,unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 9/5)
        else:
            return "Unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.temperatura,self.umedida)
    
    def unidaddeMedida (self,uniM = None):
        if uniM == None:
            return self.__umedida
        else:
            if uniM == 'F' or uniM == 'C':
                self.__umedida = uniM
                
    def temp (self,temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temp
            
    def mide (self,uniM = None):
        if uniM == None or uniM == self.__umedida:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__umedida)
            else:
                return self.__str__()
        