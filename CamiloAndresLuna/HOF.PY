def saludar():
    return "Hola"


def ejecutar(funcion):
    return funcion()


print(ejecutar(saludar))


def multiplicar_por_dos(numero):
    return numero * 2


def aplicar_operacion(funcion,  valor):
    return funcion(valor)


ressultado = aplicar_operacion(multiplicar_por_dos, 5)
print(ressultado) 