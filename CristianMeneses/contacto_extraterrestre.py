# ============================================================
#   SIMULADOR DE PRIMER CONTACTO EXTRATERRESTRE
# ============================================================

print("=" * 55)
print("   SIMULADOR DE PRIMER CONTACTO EXTRATERRESTRE")
print("=" * 55)
print()

# --- Recolección de datos ---
nombre_nave = input("Nombre de la nave extraterrestre: ")
nivel_tech = int(input("Nivel tecnológico de la nave (0-100): "))
nivel_amenaza = int(input("Nivel de amenaza del extraterrestre (0-10): "))
planeta_origen = input("Planeta de origen (Marte / Venus / Kepler / Desconocido): ").strip().capitalize()

print()
print("-" * 55)

# ============================================================
# PUNTO 1 — Condicional SIMPLE (if)
# Verifica si la nave tiene tecnología suficiente para comunicarse
# ============================================================
print("\n[1] ANÁLISIS TECNOLÓGICO DE LA NAVE")

if nivel_tech >= 70:
    print(f" La nave '{nombre_nave}' posee tecnología avanzada.")
    print("  Se puede establecer comunicación interestelar.")

# ============================================================
# PUNTO 2 — Condicional COMPUESTO (if / else)
# Determina si el extraterrestre puede ingresar a la nave humana
# ============================================================
print("\n[2] EVALUACIÓN DE AMENAZA")

if nivel_amenaza <= 4:
    print(" Nivel de amenaza BAJO. El extraterrestre puede")
    print("  ingresar a la nave humana de forma segura.")
else:
    print(" Nivel de amenaza ALTO. Acceso a la nave humana")
    print("  DENEGADO. Se mantiene contacto externo.")

# ============================================================
# PUNTO 3 — Condicional MÚLTIPLE (if / elif / else)
# Clasifica el tipo de extraterrestre según su planeta de origen
# ============================================================
print("\n[3] CLASIFICACIÓN POR PLANETA DE ORIGEN")

if planeta_origen == "Marte":
    print(" Clasificación: MARCIANO")
    print("  Especie conocida — protocolo de contacto estándar.")
elif planeta_origen == "Venus":
    print(" Clasificación: VENUSIANO")
    print("  Especie registrada — entorno de alta temperatura.")
elif planeta_origen == "Kepler":
    print(" Clasificación: KEPLERIANO")
    print("  Especie nueva — se activa protocolo de primer contacto.")
elif planeta_origen == "Desconocido":
    print(" Clasificación: ORIGEN DESCONOCIDO")
    print("  Sin registros previos — máxima alerta científica.")
else:
    print(" Clasificación: NO IDENTIFICADO")
    print("  Planeta no registrado en la base de datos galáctica.")

# ============================================================
# PUNTO 4 — match case
# El operador selecciona una acción frente al contacto
# ============================================================
print("\n[4] SELECCIÓN DE ACCIÓN")
print("  1. Establecer comunicación")
print("  2. Analizar la nave")
print("  3. Enviar un mensaje de paz")
print("  4. Finalizar el contacto")
print("  5. Desconocido — activar protocolo de emergencia")

accion = input("\nIngrese el número de la acción a realizar: ").strip()

if accion.isdigit():
    accion = int(accion)

    print()
    match accion:
        case 1:
            print(" Estableciendo comunicación con el extraterrestre...")
            print("   Traduciendo señales de radio cuántica.")
        case 2:
            print(" Analizando la nave del extraterrestre...")
            print("   Escaneando propulsión y materiales desconocidos.")
        case 3:
            print(" Enviando un mensaje de paz al extraterrestre...")
            print("   Transmitiendo coordenadas de buena voluntad.")
        case 4:
            print(" Finalizando el contacto con el extraterrestre...")
            print("   Cerrando canales de comunicación. Hasta pronto.")
        case 5:
            print(" ORIGEN DESCONOCIDO — Protocolo de emergencia activado.")
            print("   Todas las unidades en alerta máxima.")
        case _:
            print(" Opción no válida. Seleccione un número del 1 al 5.")
else:
    print("\n Entrada no válida. Debe ingresar un número entero.")

print()
print("=" * 55)
print("   FIN DE LA SIMULACIÓN")
print("=" * 55)
