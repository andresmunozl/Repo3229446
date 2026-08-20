#Ia

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

    return "Candidato: " + nombre + \
           "\nNivel promedio: " + str(nivel) + \
           "\nResultado: " + resultado

nivel_py = int(input("ingrese en números su nivel de python donde 0 es nulo conocimiento y 100 eres un gran maestro"))
nivel_math = int(input("ingrese en números su nivel de conocimiento en matematicas donde 0 es nulo conocimiento y 100 eres un gran maestro"))
experiencia_ia = input("Tiene experiencia con proyectos de IA y/n")

nombre_candidato = input("Ingrese su nombre: ")


resultado = sistema_ia(
    nombre = nombre_candidato,
    python = nivel_py,
    matematicas = nivel_math,
    experiencia = experiencia_ia
)

print(resultado)