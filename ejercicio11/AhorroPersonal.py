## Clase AhorroPersonal:  Atributo saldoInicial. Métodos para agregarInteres(tasa) y previsionAnual(). 
class AhorroPersonal:
    
    def __init__(self, saldoInicial):
        self.saldoInicial = saldoInicial
        }

        
    ## metodo para agregar interes al saldo inicial
    
    def agregarInteres(self, tasa):
        self.saldoInicial += self.saldoInicial * (tasa / 100)
    
    ## metodo para calcular la prevision anual del ahorro personal
    def previsionAnual(self):
        return self.saldoInicial * 12