def calcular_nivel(python,matematicas):
    promedio = (python + matematicas) / 2
    return promedio

def evaluar (nivel , experiencia ):
    if nivel >= 85 and experiencia >= 5:
        return "Acceso total"
    elif nivel >= 70:
        return "Acceso limitado"
    return "Acceso denegado"
