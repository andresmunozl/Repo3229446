## Clase CalculadoraVelocidad: Atributos distancia y tiempo. Método para calcularVelocidadMedia().. 
class CalculadoraVelocidad:

    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo

    def calcularVelocidadMedia(self):
        return self.distancia / self.tiempo


vel = CalculadoraVelocidad(100, 2)
print("Velocidad media es:", vel.calcularVelocidadMedia(), "m/s")