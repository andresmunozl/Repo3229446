class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def obtenerIndice(self):
        return round(self.peso / (self.altura ** 2), 2)

# 1. Crear objeto
calc = CalculadoraIMC(70, 1.75)

# 2. Llamar método
imc = calc.obtenerIndice()

# 3. Mostrar resultado
print("Tu IMC es:", imc)
