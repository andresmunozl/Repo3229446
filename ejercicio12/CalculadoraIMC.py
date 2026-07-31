class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def obtenerIndice(self):
        return round(self.peso / (self.altura ** 2), 2)
