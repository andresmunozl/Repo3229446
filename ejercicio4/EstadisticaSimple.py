## Clase EstadisticaSimple:  Atributos num1, num2, num3. Método para calcularPromedio(). 

class EstadisticaSimple:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calcularPromedio(self):
        promedio = (self.num1 + self.num2 + self.num3) 
        return promedio

dato = EstadisticaSimple(10, 20, 30)

print("Número 1:", dato.num1)
print("Número 2:", dato.num2)
print("Número 3:", dato.num3)
print("Promedio:", dato.calcularPromedio())