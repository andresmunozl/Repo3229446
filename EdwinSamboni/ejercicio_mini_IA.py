def calcular_nivel(python, matematicas):
    return (python + matematicas) / 2


def evaluar_experiencia(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return "Acceso Total"
    elif nivel >= 70:
        return "Acceso Limitado"
    return "Acceso Denegado"


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    acceso = evaluar_experiencia(nivel, experiencia)
    return f"{nombre}: nivel {nivel:.1f}. {acceso}"


if __name__ == "__main__":
    resultado = sistema_ia(
        nombre="Edwin",
        python=90,
        matematicas=88,
        experiencia=True,
    )
    print(resultado)
