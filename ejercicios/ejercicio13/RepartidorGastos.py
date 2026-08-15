##  Clase RepartidorGastos: Atributos totalFactura y numeroPersonas. Método para divisionEquitativa(). 
class RepartidorGastos:
    
    def __init__(self, totalFactura, numeroPersonas):
        self.totalFactura = totalFactura
        self.numeroPersonas = numeroPersonas
    
    def divisionEquitativa(self):
        return self.totalFactura / self.numeroPersonas


# Programa principal con valores fijos
reparto = RepartidorGastos(100, 4)

print("Total factura:", reparto.totalFactura)
print("Número de personas:", reparto.numeroPersonas)
print("Cada persona paga:", reparto.divisionEquitativa())