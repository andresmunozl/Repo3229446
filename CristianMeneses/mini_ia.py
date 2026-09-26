def calcular_nivel(python, matematicas):
    promedio = (python + matematicas)/2
    return promedio

def evaluar(experiencia: bool, promedio:float = 0):
    if promedio >= 85 and experiencia == True:
        return 'Acceso Total'
    elif promedio >= 70: 
        return 'Acceso Limitado'
    else: 
        return 'Acceso Denegado'

# experiencia = bool(input('ingrese su experiencia'))

def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    acceso = evaluar(experiencia, nivel)
    return f"{nombre}: nivel {nivel:.1f}. {acceso}"

if __name__ == "__main__": 
    nivel_python = float(input('ingrese su nivel de python (0-100)'))
    nivel_matematicas = float(input('ingrese su nivel de matematicas (0-100)'))
    respuesta = input('¿Tiene experiencia? (si/no): ').strip().lower()
    experiencia = respuesta == 'si' # convierte texto a bool correctamente

    resultado = sistema_ia(
        nombre="Cristian",
        python=nivel_python,
        matematicas=nivel_matematicas,
        experiencia=experiencia,
    )
    print(resultado)
