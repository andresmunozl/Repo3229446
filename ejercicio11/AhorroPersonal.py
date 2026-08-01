class AhorroPersonal:
    """Cuenta de ahorro con interés anual."""

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def agregarInteres(self, tasa):
        """Aplica interés anual al saldo actual."""
        self.saldo *= (1 + tasa / 100)

    def previsionAnual(self):
        """Proyección simple: saldo actual * 12."""
        return self.saldo * 12


# ---- Programa principal ----
if __name__ == "__main__":
    print("=== AHORRO PERSONAL ===")
    saldo_inicial = float(input("Ingrese el saldo inicial: $"))
    tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))

    print(f"\nSaldo inicial: ${saldo_inicial:.2f}")
    print(f"Tasa de interés: {tasa_interes:.2f}%\n")

    ahorro = AhorroPersonal(saldo_inicial)
    ahorro.agregarInteres(tasa_interes)
    print(f"Saldo con interés: ${ahorro.saldo:.2f}")

    prevision = ahorro.previsionAnual()
    print(f"Previsión anual (saldo * 12): ${prevision:.2f}")