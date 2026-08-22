def calcular_nivel(python, matematicas):
    promedio = (python + matematicas) / 2
    return promedio


def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return 'Acceso total'
    elif nivel >= 70:
        return 'Acceso Limitado'
    else:
        return 'Acceso Denegado'


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    resultado = evaluar(nivel, experiencia)
    return nombre + ':' + resultado


print(sistema_ia(nombre='Camilo', python=80, matematicas=90, experiencia=True))
print(sistema_ia(nombre='Carlos', python=50, matematicas=60, experiencia=False))
print(sistema_ia(nombre='Andres', python=80, matematicas=70, experiencia=True))
