def convertir_farenheit_a_celsius(nombre, grados_f: int = 10000):
    celsius = (grados_f - 32) / 1.8
    return celsius


# resultado = convertir_farenheit_a_celsius(100) + 10
# print(resultado)
# convertir_farenheit_a_celsius(70)
# grados = 100
grados = int(input('Ingrese los graods en farenheit'))
print(convertir_farenheit_a_celsius(grados_f=10, nombre='Bartolo'))
print(convertir_farenheit_a_celsius('Camilo'))
