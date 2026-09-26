def convertir_fahrenheit_a_celsius(nombre, grados_f: int = 10000):
    celsius = (grados_f-32)/1.8
    return celsius


# resultado = convertir_fahrenheit_a_celsius(100) + 10
# print(resultado)
# grados = 100
grados = int(input('ingrese los grados en fahrenheit'))

print(convertir_fahrenheit_a_celsius(grados_f=10, nombre='Arnulfo'))
print(convertir_fahrenheit_a_celsius('andres'))


# En otra linea temporal

# def convertir_fahrenheit_a_celsius(grados_f):
#    celsius = (grados_f-32)/1.8
#    print(celsius)
    
# convertir_fahrenheit_a_celsius(100)

