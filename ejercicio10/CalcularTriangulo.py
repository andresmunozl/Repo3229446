class CalcularTriangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2


# ✅ BIEN - El código de prueba solo se ejecuta si ejecutas ESTE archivo directamente
if __name__ == "__main__":
    # Este código SOLO se ejecuta cuando ejecutas este archivo directamente
    # NO se ejecuta cuando haces "import"
    base = float(input("Base triangulo: "))
    altura = float(input("Altura triangulo: "))
    
    triangulo = CalcularTriangulo(base, altura)
    print(f"Área: {triangulo.calcularArea()}")