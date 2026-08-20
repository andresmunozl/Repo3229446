def convertir_far_a_celcius(grados_f: int = 10000):
    celcius = (grados_f - 32) / 1.8
    return celcius


# resultado = convertir_far_a_celcius(100) + 10
# print(resultado)  
grados = int(input('Ingresa los grados en fahrenheit'))
print(convertir_far_a_celcius(grados_f=10, nombre='camilo'))
print(convertir_far_a_celcius('andres'))
