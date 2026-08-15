# EJERCICIO DE CONDICIONALES

# CONDICIONAL SIMPLE
tecnologia_nave = input("Ingrese la tecnología de la nave (avanzada/basica): ")
if tecnologia_nave == "avanzada":
    print("Tecnología suficiente. Es posible iniciar comunicación.")

# CONDICIONAL COMPUESTA
nivel_amenaza = int(input("Ingrese el nivel de amenaza del extraterrestre 1/3 : "))
if nivel_amenaza >= 3:
    print(" Alto. No se permite el ingreso a la nave.")
else:
    print(" Aceptable. Se permite el ingreso a la nave.")

# CONDICIONAL MULTIPLE
planeta_origen = input("Ingrese el planeta de origen (Marte/saturno/pluton): ")
if planeta_origen == "Marte":
    print("Clasificación: especie marciana.")
elif planeta_origen == "Saturno":
    print("Clasificación: especie saturnania.")
elif planeta_origen == "Pluton":
    print("Clasificación: especie plutoniana.")
else:
    print("Clasificación: especie de fuera de este universo.")

# MATCH CASE
accion = int(input("Seleccione una acción (1: Establecer comunicación, 2: Analizar la nave, 3: Enviar mensaje de paz, 4: Finalizar contacto): "))
match accion:
    case 1:
        print("Acción seleccionada: Establecer comunicación.")
    case 2:
        print("Acción seleccionada: Analizar la nave.")
    case 3:
        print("Acción seleccionada: Enviar mensaje de paz.")
    case 4:
        print("Acción seleccionada: Finalizar contacto.")
    case _:
        print("Opción no válida. Intente nuevamente con un número del 1 al 4.")