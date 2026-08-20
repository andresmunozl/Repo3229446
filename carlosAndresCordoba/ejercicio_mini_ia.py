def calcular_nivel(python, matematicas):
    return (python + matematicas) / 2


def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return "Acceso Total"
    elif nivel >= 70:
        return "Acceso Limitado"
    else:
        return "Acceso Denegado"


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    resultado = evaluar(nivel, experiencia)
    return nombre + ": " + resultado


print(sistema_ia(nombre="Andres", python=90, matematicas=88, experiencia=True))
print(sistema_ia(nombre="Laura", python=75, matematicas=65))
print(sistema_ia("Carlos", python=40, matematicas=50))