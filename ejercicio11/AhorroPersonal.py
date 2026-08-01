class AhorroPersonal:
    """Cuenta de ahorro con interés anual."""

    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.saldo = saldo_inicial  # nombre más claro

    def agregar_interes(self, tasa):
        """Aplica interés anual (una vez) al saldo actual."""
        if tasa < 0:
            raise ValueError("La tasa no puede ser negativa.")
        self.saldo *= (1 + tasa / 100)

    def prevision_anual(self):
        """
        Devuelve una proyección simple (saldo actual * 12).
        Nota: esta fórmula no es realista; se mantiene por compatibilidad.
        """
        return self.saldo * 12


# ---- Datos quemados ----
saldo_inicial = 1000.0
tasa_interes = 5.0

print("=== AHORRO PERSONAL (DATOS QUEMADOS) ===")
print(f"Saldo inicial: ${saldo_inicial:.2f}")
print(f"Tasa de interés: {tasa_interes:.2f}%\n")

ahorro = AhorroPersonal(saldo_inicial)

ahorro.agregar_interes(tasa_interes)
print(f"Saldo con interés: ${ahorro.saldo:.2f}")

prevision = ahorro.prevision_anual()
print(f"Previsión anual (saldo * 12): ${prevision:.2f}")