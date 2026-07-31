## Clase OperacionesPotencia:  Atributos base y exponente. Métodos para calcularPotencia() y calcularCuadrado(). 
class OperacionesPotencia:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcularPotencia(self):
        return self.base ** self.exponente

    def calcularCuadrado(self):
        return self.base ** 2