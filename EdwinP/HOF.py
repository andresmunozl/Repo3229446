def saludar():
    return "Hola"

def ejecutar(funcion):
    return funcion()

print(ejecutar(saludar))

#Pasar funciones como argumento 

def multiplicar_por_dos(numero):
    return numero  * 2

def aplicar_operacion (funcion, valor):
    return funcion(valor)

resultado = aplicar_operacion(multiplicar_por_dos, 5)
print(resultado)

