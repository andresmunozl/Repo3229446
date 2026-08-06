import unittest

# 1. IMPORTACIONES DE CADA EJERCICO

import sys
from io import StringIO


<<<<<<< HEAD
# 2. CLASE DE PRUEBAS

class TestTallerGrupal(unittest.TestCase):

    # --- EJERCICIO 1 ---
    def test_ejercicio1_calculadora_basica(self):
        calc = CalculadoraBasica()
        self.assertEqual(calc.sumar(10, 5), 15)
        self.assertEqual(calc.restar(10, 5), 5)

    # --- EJERCICIO 2 ---
    def test_ejercicio2_area_cuadrado(self):
        cuadrado = CalculadoraAreaCuadrado(4)
        self.assertEqual(cuadrado.calcularArea(), 16)
        self.assertEqual(cuadrado.calcularPerimetro(), 16)

    # --- EJERCICIO 3 ---
    def test_ejercicio3_conversor_temperatura(self):
        temp = ConversorTemperatura(0)
        self.assertEqual(temp.aFahrenheit(), 32)
        self.assertEqual(temp.aKelvin(), 273.15)

    # --- EJERCICIO 4 ---
    def test_ejercicio4_estadistica_simple(self):
        est = EstadisticaSimple(10, 20, 30)
        self.assertEqual(est.calcularPromedio(), 20)

    # --- EJERCICIO 5 ---
    def test_ejercicio5_calculadora_iva(self):
        iva = CalculadoraIVA(100)
        self.assertEqual(iva.calcularIVA(), 21)
        self.assertEqual(iva.precioTotal(), 121)

    # --- EJERCICIO 6 ---
    def test_ejercicio6_operaciones_potencia(self):
        pot = OperacionesPotencia(2, 3)
        self.assertEqual(pot.calcularPotencia(), 8)
        self.assertEqual(pot.calcularCuadrado(), 4)

    # --- EJERCICIO 7 ---
    def test_ejercicio7_calculadora_descuentos(self):
        desc = CalculadoraDescuentos(100, 20)
        self.assertEqual(desc.montoDescuento(), 20)
        self.assertEqual(desc.precioFinal(), 80)

    # --- EJERCICIO 8 ---
    def test_ejercicio8_geometria_circulo(self):
        circulo = GeometriaCirculo(3)
        self.assertAlmostEqual(circulo.area(), 28.274, places=2)
        self.assertAlmostEqual(circulo.circunferencia(), 18.849, places=2)

    # --- EJERCICIO 9 ---
    def test_ejercicio9_convertidor_medidas(self):
        medidas = ConvertidorMedidas(2)
        self.assertEqual(medidas.aCentimetros(), 200)
        self.assertEqual(medidas.aKilometros(), 0.002)

    # --- EJERCICIO 10 ---
    def test_ejercicio10_calculadora_triangulo(self):
        triangulo = CalcularTriangulo(10, 5)
        self.assertEqual(triangulo.calcularArea(), 25)

    # --- EJERCICIO 11 ---
    def test_ejercicio11_ahorro_personal(self):
        ahorro = AhorroPersonal(1000)
        ahorro.agregarInteres(10)  # 10% de interés
        # CORREGIDO: 1000 + 10% = 1100, 1100 * 12 meses = 13200
        self.assertEqual(ahorro.previsionAnual(), 13200)  # ✅ AHORA SÍ

    # --- EJERCICIO 12 ---
    def test_ejercicio12_calculadora_imc(self):
        imc = CalculadoraIMC(70, 1.75)
        self.assertAlmostEqual(imc.obtenerIndice(), 22.86, places=2)

    # --- EJERCICIO 13 ---
    def test_ejercicio13_repartidor_gastos(self):
        gastos = RepartidorGastos(100, 4)
        self.assertEqual(gastos.divisionEquitativa(), 25)

    # --- EJERCICIO 14 ---
    def test_ejercicio14_calculadora_velocidad(self):
        vel = CalculadoraVelocidad(100, 2)
        self.assertEqual(vel.calcularVelocidadMedia(), 50)

    # --- EJERCICIO 15 ---
    def test_ejercicio15_analisis_numerico(self):
        numero = AnalisisNumerico(4)
        self.assertTrue(numero.esPar())
        self.assertEqual(numero.obtenerDoble(), 8)
        
        numero_impar = AnalisisNumerico(7)
        self.assertFalse(numero_impar.esPar())
        self.assertEqual(numero_impar.obtenerDoble(), 14)
=======
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
>>>>>>> 2a21a3166ffa5c4a35005b95980d30b0e3ec35c4


if __name__ == '__main__':
    main()