
print("   PRIMER CONTACTO CON UNA CIVILIZACIÓN")


# Datos de la nave extraterrestre
tecnologia = int(input("Ingrese el nivel de tecnología de la nave (1 a 100):"))

# 1. CONDICIONAL SIMPLE
if tecnologia >= 70:
    print("La tecnología es suficientemente avanzada para establecer comunicación")

# Datos del extraterrestre
amenaza = int(input("Ingrese el nivel de amenaza del extraterrestre (1 a 100):"))

# 2. CONDICIONAL COMPUESTO
if amenaza <= 50:
    print("El extraterrestre puede ingresar a la nave humana.")
else:
    print("El extraterrestre NO puede ingresar a la nave humana.")

# Datos del planeta
planeta = input("Ingrese el planeta de origen del extraterrestre: ")

# 3. CONDICIONAL MÚLTIPLE
if planeta == "marte":
    print("Tipo de extraterrestre: marciano")
elif planeta == "venus":
    print("Tipo de extraterrestre: venusiano")
elif planeta == "jupiter":
    print("Tipo de extraterrestre: jupiteriano")
else:
    print("Tipo de extraterrestre: Extraterrestre desconocido")

# 4. MATCH CASE
print()
print("Seleccione una acción:")
print("1. Establecer comunicación")
print("2. Analizar la nave")
print("3. Enviar un mensaje de paz")
print("4. Finalizar el contacto")

opcion = int(input("Ingrese una opción: "))

match opcion:
    case 1:
        print("Se ha establecido comunicación con la civilización ")
    case 2:
        print("Analizando la nave extraterrestre...")
    case 3:
        print("Mensaje enviado: ¡Venimos en son de paz!")
    case 4:
        print("El contacto extraterrestre ha finalizado.")
    case _:
        print("Opción no válida.")

