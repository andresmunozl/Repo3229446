## Clase CalculadoraDescuentos:  Atributos precio y porcentaje. Método para montoDescuento() y precioFinal(). 
class CalculadoraDescuentos:

    def montoDescuento(precio, porcentaje):
        return precio * porcentaje /100

    def precioFinal(precio, porcentaje):
        descuento = precio * porcentaje / 100
        return precio - descuento

print(f"Descuento:",CalculadoraDescuentos.montoDescuento(100, 20))
print(f"Precio Final:",CalculadoraDescuentos.precioFinal(100,20))