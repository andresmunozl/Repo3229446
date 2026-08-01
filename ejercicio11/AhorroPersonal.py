## Clase AhorroPersonal:  Atributo saldoInicial. Métodos para agregarInteres(tasa) y previsionAnual(). 
class AhorroPersonal:
    
    def __init_11_(self, saldoInicial):
        self.saldoInicial = saldoInicial
    
    def agregarInteres(self, tasa):
        self.saldoInicial += self.saldoInicial * (tasa / 100)
    
    def previsionAnual(self):
        return self.saldoInicial * 12

# Programa principal
print("=== AHORRO PERSONAL ===")

saldo = float(input("Saldo inicial: "))
tasa = float(input("Tasa de interés (%): "))

ahorro = AhorroPersonal(saldo)

print("\n--- RESULTADOS ---")
print(f"Saldo inicial: ${saldo:.2f}")

ahorro.agregarInteres(tasa)
print(f"Saldo con interés: ${ahorro.saldoInicial:.2f}")

prevision = ahorro.previsionAnual()
print(f"Previsión anual: ${prevision:.2f}")