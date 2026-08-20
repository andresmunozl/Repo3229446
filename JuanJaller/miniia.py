# 1
def calcular_nivel(python, matematicas):
    promedio = (python + matematicas) / 2
    return promedio

# 2

def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return "Acceso total"
    elif nivel >= 70:
        return "Acceso limitado"
    else:
        return "Acceso prohibido"

#3
def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    resultado = evaluar(nivel, experiencia)
    return f"{nombre} {nivel} {resultado}"

print(sistema_ia("juan", python=85, matematicas=80, experiencia=True))
print(sistema_ia("david", python=45, matematicas=60))
print(sistema_ia(nombre="alex", python=50, matematicas=60))
