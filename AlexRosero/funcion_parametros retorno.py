#def convertir_fahreneit_a_celsius(grados_f):
    #celsius = (grados_f - 32)/1.8
    #print(celsius)
 #   return 

#convertir_fahreneit_a_celsius(100)

def convertir_fahreneit_a_celsius(nombre, grados_f:int = 1000):
    celsius = (grados_f - 32)/1.8
    return celsius, nombre

#grados = 

grados = int(input("ingrese los grados en fahreneit"))

resultado=convertir_fahreneit_a_celsius(grados)
print(convertir_fahreneit_a_celsius('alex'))
print(convertir_fahreneit_a_celsius('alex',grados_f=10))

print(resultado)