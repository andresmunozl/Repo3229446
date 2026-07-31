## Clase CalculadoraTriangulo:  Atributos base y altura. Método para calcularArea() ().
class CalculadoraTriangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura / 2


base = float(input("Base triangulo: "))
altura = float(input("Altura triangulo: "))

triangulo = CalculadoraTriangulo(base, altura)
print("El area es: ", triangulo.calcularArea())
