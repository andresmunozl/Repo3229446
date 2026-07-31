## Clase ConvertidorMedidas:  Atributo metros. Métodos para aCentimetros() y aKilometros(). 
class Convertidormedidad:
    
    def __init__(self, metros):
        self.metros = metros
        
    ## metodo para la conversion de los metros a centimetros
    
    def aCentimetros(self):
        return self.metros * 100    
    
    ## metodo para la conversion de los metros a kilometros
    def aKilometros(self):
        return self.metros / 1000