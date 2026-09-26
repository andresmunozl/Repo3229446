def calcular_nivel(python, matematicas):
    promedio = (python + matematicas) / 2
    return (promedio)

def evualar (nivel, experiencia):
    if nivel >= 85 and experiencia:
        return('accso total')
    elif nivel >= 70:
        return('acceso limitado')
    else:
        return('acceso denegado')


def sistema_ia (nombre,python, matematicas, experiencia=False):

    nivel_general = calcular_nivel(python, matematicas)

    decision = evualar(nivel_general, experiencia)

    print(f"Aspirante : {nombre} | Nivel general : {nivel_general}' | desicion : {decision}")


sistema_ia(nombre="andres", python=87, matematicas=90 , experiencia= True)









