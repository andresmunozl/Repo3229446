# funcion con retorno
#def convertir_fahreneit_a_cesius (grados_f):
 #   celsiius = ((grados_f - 32)/1.8)
  #  resultado = celsiius + 10
   # print(resultado)

#convertir_fahreneit_a_cesius(100)

def convertir_fahreneit_a_cesius(nombre, grados_f: int = 10000):
    celsius = (grados_f - 32) / 1.8
    return celsius

grados = int(input("ingrese grados : "))
print(convertir_fahreneit_a_cesius(nombre='andres',grados_f=10))
