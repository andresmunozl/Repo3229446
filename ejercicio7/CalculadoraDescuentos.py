## Clase CalculadoraDescuentos:  Atributos precio y porcentaje. Método para montoDescuento() y precioFinal(). 
class CalculadoraDescuentos:

    def __init__(self, precio, porcentaje):
        self.precio = precio
        self.porcentaje = porcentaje

    def montoDescuento(self):
        return self.precio * self.porcentaje / 100

    def precioFinal(self):
        descuento = self.montoDescuento()
        return self.precio - descuento

dato = CalculadoraDescuentos(100, 20)

print(f"Descuento:", dato.montoDescuento())
print(f"Precio Final:", dato.precioFinal())