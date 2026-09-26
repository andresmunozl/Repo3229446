def convertir_fahrenheit_a_celsius(grados_f):
    celsius = (grados_f - 32) / 1.8
    return celsius

resultado = convertir_fahrenheit_a_celsius(100)
print(resultado)
