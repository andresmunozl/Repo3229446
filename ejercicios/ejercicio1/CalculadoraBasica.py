
class CalculadoraBasica:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b


if __name__ == "__main__":
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))

    calculadora = CalculadoraBasica()
    print("Suma:", calculadora.sumar(a, b))
    print("Resta:", calculadora.restar(a, b))
