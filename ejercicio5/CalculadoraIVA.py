## Clase CalculadoraIVA:  Atributo precioBase. Métodos para obtenerIVA(21%) y precioTotal().
class CalculadoraIVA:
    def __init__(self, precio_producto, iva = 0.19):
        self.precio_producto = precio_producto
        self.iva = iva
        
    def calculariva(self):
      iva = (self.precio_producto * self.iva)
      return iva

<<<<<<< HEAD
datos = CalculadoraIVA(12800, 0.19)
=======
datos = CalculadoaIVA(12800, 0.19)
>>>>>>> df8834c254b9e4b4c71ec55a952a2a360ad06027
resultado = datos.calculariva()
print(f"El IVA es : {resultado}")

