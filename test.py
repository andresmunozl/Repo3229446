import unittest

# 1. IMPORTACIONES DE CADA EJERCICO

from ejercicio1.CalculadoraBasica import CalculadoraBasica
from ejercicio2.CalculadoraAreaCuadrado import CalculadoraAreaCuadrado
from ejercicio3.ConversorTemperatura import ConversorTemperatura
from ejercicio4.EstadisticaSimple import EstadisticaSimple
from ejercicio5.CalculadoraIVA import CalculadoraIVA
from ejercicio6.OperacionesPotencia import OperacionesPotencia
from ejercicio7.CalculadoraDescuentos import CalculadoraDescuentos
from ejercicio8.GeometriaCirculo import GeometriaCirculo
from ejercicio9.ConvertidorMedidas import ConvertidorMedidas
from ejercicio10.CalcularTriangulo import CalcularTriangulo
from ejercicio11.AhorroPersonal import AhorroPersonal
from ejercicio12.CalculadoraIMC import CalculadoraIMC
from ejercicio13.RepartidorGastos import RepartidorGastos
from ejercicio14.CalculadoraVelocidad import CalculadoraVelocidad
from ejercicio15.AnalisisNumerico import AnalisisNumerico


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
        self.assertEqual(iva.obtenerIVA(), 21)
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


# ==========================================
# 3. EJECUCIÓN DEL SCRIPT
# ==========================================
if __name__ == '__main__':
    unittest.main()