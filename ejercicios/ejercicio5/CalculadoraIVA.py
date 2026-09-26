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
>>>>>>> d2b6644aa3faf81f11a7f8d05a92e69e01dfc3a2
print(f"El IVA es : {resultado}")
print(f"El precio total es: {datos.precioTotal()}")

