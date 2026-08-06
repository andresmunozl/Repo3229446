## Clase CalculadoraDescuentos:  Atributos precio y porcentaje. Método para montoDescuento() y precioFinal(). 
class CalculadoraDescuentos:

    def montoDescuento(precio, porcentaje):
        return precio * porcentaje /100

    def precioFinal(precio, porcentaje):
        descuento = precio * porcentaje / 100
        return precio - descuento


    def precioFinal(self):
        descuento = self.montoDescuento()
        return self.precio - descuento

dato = CalculadoraDescuentos(100, 20)

print(f"Descuento:", dato.montoDescuento())
print(f"Precio Final:", dato.precioFinal())

