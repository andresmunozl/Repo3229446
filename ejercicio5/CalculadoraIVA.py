## Clase CalculadoraIVA:  Atributo precioBase. Métodos para obtenerIVA(21%) y precioTotal().
class CalculadoraIVA:
    def __init__(self, precio_producto, iva = 0.19):
        self.precio_producto = precio_producto
        self.iva = iva
        
    def calcularIVA(self):
      iva = (self.precio_producto * self.iva)
      return iva
    def precioTotal(self):
        return self.precio_producto + self.calcularIVA()

datos = CalculadoraIVA(12800, 0.19)


print(f"El IVA es : {resultado}")
print(f"El precio total es: {datos.precioTotal()}")

