def calcular_nivel(python, matematicas):
    promedio = (python + matematicas) / 2
    return promedio


def evaluar(nivel, experiencia):
    if nivel >= 85:
        if experiencia:
            return "Acceso Total"
        else:
            return "Acceso Limitado"
    elif nivel >= 70:
        return "Acceso Limitado"
    else:
        return "Acceso Denegado"


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    resultado = evaluar(nivel, experiencia)

    return f"{nombre}: {resultado}"


nombre = input("Ingrese su nombre: ")

python = float(input("Ingrese su nivel de Python: "))

matematicas = float(input("Ingrese su nivel de Matemáticas: "))

experiencia = input("¿Tiene experiencia en IA? (si/no): ")

if experiencia == "si":
    experiencia = True
else:
    experiencia = False


resultado = sistema_ia(
    nombre=nombre,
    python=python,
    matematicas=matematicas,
    experiencia=experiencia
)

print(resultado)