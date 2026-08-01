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
<<<<<<< HEAD
resultado = datos.calculariva()
=======
resultado = datos.calcularIVA()
>>>>>>> b5dc6a92f5c07698b3137d89c82bf2ef3dde9a84
print(f"El IVA es : {resultado}")
print(f"El precio total es: {datos.precioTotal()}")

