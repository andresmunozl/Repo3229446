
print("   PRIMER CONTACTO EXTRATERRESTRE    ")


tecnologia = int(input("Ingrese el nivel tecnológico de la nave en una escala de (1-10): "))

#  el condicional simple (if)
if tecnologia >= 7:
    print("La tecnología es suficientemente avanzada para establecer comunicación.")


amenaza = int(input("Ingrese el nivel de amenaza del extraterrestre (1-10): "))

# el condicional compuesto (if/else)
if amenaza <= 5:
    print("El extraterrestre puede ingresar a la nave humana.")
else:
    print("El extraterrestre NO puede ingresar a la nave humana.")


planeta = input("Ingrese el planeta de origen (Marte, Venus o Jupiter): ")

# el condicional múltiple (if/elif/else)
if planeta == "Marte":
    print("El extraterrestre es de tipo marciano.")
elif planeta == "Venus":
    print("El extraterrestre es de tipo venusino.")
elif planeta == "Jupiter":
    print("El extraterrestre es de tipo joviano.")
else:
    print("El planeta de origen es desconocido.")


print()
print("¿Qué desea hacer frente al contacto?")
print("1. Establecer comunicación")
print("2. Analizar la nave")
print("3. Enviar un mensaje de paz")
print("4. Finalizar el contacto")

opcion = int(input("Seleccione una opción: "))

# Match case
match opcion:
    case 1:
        print("Establecar comunicacion con la civilización extraterrestre.")
    case 2:
        print("Iniciar un análisis de la nave extraterrestre.")
    case 3:
        print("Enviar un mensaje de paz.")
    case 4:
        print("Finalizar el contacto con extraterrestres.")
    case _:
        print("Opcion no valida. por los nervios escogiste una equivocada. ")

print("Fin de la simulacion. contacto para ir a la luna")