## Clase ConversorTemperatura:  Atributo celsius. Métodos para aFahrenheit() y aKelvin(). 
class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
            return (self.celsius * 9/5) + 32

    def a_kelvin(self):
            return self.celsius + 273.15

mi_temp = ConversorTemperatura(25)

print("Temperatura en Fahrenheit: ", mi_temp.a_fahrenheit())
print("Temperatura en Kelvin: ", mi_temp.a_kelvin())
