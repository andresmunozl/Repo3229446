import unittest

# 1. IMPORTACIONES DE CADA EJERCICO

import sys
from io import StringIO


def importar_clase(ruta_modulo, nombre_clase):
    """Importa la clase sin mostrar los prints de los ejercicios."""
    stdout_original = sys.stdout
    sys.stdout = StringIO()
    try:
        modulo = __import__(ruta_modulo, fromlist=[nombre_clase])
        clase = getattr(modulo, nombre_clase)
    finally:
        sys.stdout = stdout_original
    return clase


def mostrar_menu():
    print("\n" + "=" * 42)
    print("         MENÚ TALLER GRUPAL")
    print("=" * 42)
    print(" 1. Calculadora Básica")
    print(" 2. Área del Cuadrado")
    print(" 3. Conversor de Temperatura")
    print(" 4. Estadística Simple")
    print(" 5. Calculadora de IVA")
    print(" 6. Operaciones de Potencia")
    print(" 7. Calculadora de Descuentos")
    print(" 8. Geometría del Círculo")
    print(" 9. Convertidor de Medidas")
    print("10. Área del Triángulo")
    print("11. Ahorro Personal")
    print("12. Calculadora de IMC")
    print("13. Repartidor de Gastos")
    print("14. Calculadora de Velocidad")
    print("15. Análisis Numérico")
    print(" 0. Salir")
    print("=" * 42)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                Clase = importar_clase("ejercicio1.CalculadoraBasica", "CalculadoraBasica")
                calc = Clase()
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Suma: {calc.sumar(a, b)}")
                print(f"Resta: {calc.restar(a, b)}")

            case "2":
                Clase = importar_clase("ejercicio2.CalculadoraAreaCuadrado", "CalculadoraAreaCuadrado")
                lado = float(input("Lado del cuadrado: "))
                obj = Clase(lado)
                print(f"Área: {obj.calcularArea()}")
                print(f"Perímetro: {obj.calcularPerimetro()}")

            case "3":
                Clase = importar_clase("ejercicio3.ConversorTemperatura", "ConversorTemperatura")
                celsius = float(input("Grados Celsius: "))
                obj = Clase(celsius)
                print(f"Fahrenheit: {obj.aFahrenheit()}")
                print(f"Kelvin: {obj.aKelvin()}")

            case "4":
                Clase = importar_clase("ejercicio4.EstadisticaSimple", "EstadisticaSimple")
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                n3 = float(input("Número 3: "))
                obj = Clase(n1, n2, n3)
                print(f"Promedio: {obj.calcularPromedio()}")

            case "5":
                Clase = importar_clase("ejercicio5.CalculadoraIVA", "CalculadoraIVA")
                precio = float(input("Precio base: "))
                obj = Clase(precio)
                print(f"IVA (21%): {obj.obtenerIVA()}")
                print(f"Precio total: {obj.precioTotal()}")

            case "6":
                Clase = importar_clase("ejercicio6.OperacionesPotencia", "OperacionesPotencia")
                base = float(input("Base: "))
                exp = int(input("Exponente: "))
                obj = Clase(base, exp)
                print(f"Potencia: {obj.calcularPotencia()}")
                print(f"Cuadrado de la base: {obj.calcularCuadrado()}")

            case "7":
                Clase = importar_clase("ejercicio7.CalculadoraDescuentos", "CalculadoraDescuentos")
                precio = float(input("Precio original: "))
                desc = float(input("Porcentaje de descuento: "))
                obj = Clase(precio, desc)
                print(f"Monto descontado: {obj.montoDescuento()}")
                print(f"Precio final: {obj.precioFinal()}")

            case "8":
                Clase = importar_clase("ejercicio8.GeometriaCirculo", "GeometriaCirculo")
                radio = float(input("Radio del círculo: "))
                obj = Clase(radio)
                print(f"Área: {obj.area():.3f}")
                print(f"Circunferencia: {obj.circunferencia():.3f}")

            case "9":
                Clase = importar_clase("ejercicio9.ConvertidorMedidas", "ConvertidorMedidas")
                metros = float(input("Metros: "))
                obj = Clase(metros)
                print(f"Centímetros: {obj.aCentimetros()}")
                print(f"Kilómetros: {obj.aKilometros()}")

            case "10":
                Clase = importar_clase("ejercicio10.CalcularTriangulo", "CalcularTriangulo")
                base = float(input("Base del triángulo: "))
                altura = float(input("Altura del triángulo: "))
                obj = Clase(base, altura)
                print(f"Área: {obj.calcularArea()}")

            case "11":
                Clase = importar_clase("ejercicio11.AhorroPersonal", "AhorroPersonal")
                saldo = float(input("Saldo inicial: "))
                tasa = float(input("Tasa de interés (%): "))
                obj = Clase(saldo)
                obj.agregarInteres(tasa)
                print(f"Previsión anual: {obj.previsionAnual()}")

            case "12":
                Clase = importar_clase("ejercicio12.CalculadoraIMC", "CalculadoraIMC")
                peso = float(input("Peso (kg): "))
                altura = float(input("Altura (m): "))
                obj = Clase(peso, altura)
                print(f"IMC: {obj.obtenerIndice():.2f}")

            case "13":
                Clase = importar_clase("ejercicio13.RepartidorGastos", "RepartidorGastos")
                total = float(input("Total de la factura: "))
                personas = int(input("Número de personas: "))
                obj = Clase(total, personas)
                print(f"Cada uno paga: {obj.divisionEquitativa()}")

            case "14":
                Clase = importar_clase("ejercicio14.CalculadoraVelocidad", "CalculadoraVelocidad")
                distancia = float(input("Distancia (km): "))
                tiempo = float(input("Tiempo (horas): "))
                obj = Clase(distancia, tiempo)
                print(f"Velocidad media: {obj.calcularVelocidadMedia()} km/h")

            case "15":
                Clase = importar_clase("ejercicio15.AnalisisNumerico", "AnalisisNumerico")
                numero = int(input("Número entero: "))
                obj = Clase(numero)
                print(f"¿Es par? {obj.esPar()}")
                print(f"Doble: {obj.obtenerDoble()}")

            case "0":
                print("¡Hasta luego!")
                break

            case _:
                print("Opción no válida. Intenta de nuevo.")

        input("\nPresiona ENTER para continuar...")


if __name__ == '__main__':
    main()