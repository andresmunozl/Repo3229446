##  Clase GeometriaCirculo: Atributo radio. Métodos para area() () y circunferencia().


class GeometriaCirculo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        resultado = 3.1416 * self.radio**2
        return resultado

    def circunferencia(self):

        return 2 * 3.1416 * self.radio


radio_usuario = int(input("Ingrese el radio del circulo: "))
c = GeometriaCirculo(radio_usuario)
print(c.area())
print(c.circunferencia())
