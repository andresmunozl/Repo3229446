## Clase CalculadoraIVA:  Atributo precioBase. Métodos para obtenerIVA(21%) y precioTotal().
class CalculadorIVA:
    def __init__(self, precio_producto, iva = 0.19):
        self.precio_producto = precio_producto
        self.iva = iva
        
    def calculariva(self):
      iva = (self.precio_producto * self.iva)
      return iva

datos = CalculadorIVA(12800, 0.19)
resultado = datos.calculariva()
print(f"El IVA es : {resultado}")

