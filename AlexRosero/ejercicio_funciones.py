def calcular_nivel(python,matematicas):
    return (python * matematicas) /2

def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
     "acesso total"
    elif nivel >= 70:
     "accesos total"
    else: "acceso denegado"

def sistema_ia(nombre, python, matematicas, experiencia = False):

    nivel_promedio = calcular_nivel(python, matematicas)
    resultado_acceso = evaluar(nivel_promedio, experiencia)


    return f"Candidato: {nombre}\nNivel promedio: {nivel_promedio:.2f}\nResultado: {resultado_acceso}"

print("Usuario con experiencia y alto nivel")

resultado1 = sistema_ia(nombre="Ana", python=90, matematicas=85, experiencia=True)
print(resultado1)

print("caso2 usuario sin experiencia ")

resultado2 =sistema_ia(nombre="alex", python=80, matematicas=70)
print(resultado2)