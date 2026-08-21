# contacto_extraterrestre.py
# Simulador de primer contacto extraterrestre

print("=== RADAR DE PRIMER CONTACTO ===")
tecnologia = int(input("Nivel de tecnologia (1-10): "))
amenaza = int(input("Nivel de amenaza (1-10): "))
planeta = input("Planeta de origen: ")

# 1. CONDICIONAL SIMPLE
print("\n--- ANALISIS DE COMUNICACION ---")
if tecnologia >= 7:
    print("Tecnologia avanzada. Comunicacion establecida.")

# 2. CONDICIONAL COMPUESTO
print("\n--- CONTROL DE ACCESO ---")
if amenaza >= 5:
    print("ALERTA: Amenaza alta. Acceso DENEGADO.")
else:
    print("Amenaza baja. Acceso PERMITIDO.")

# 3. CONDICIONAL MULTIPLE
print("\n--- CLASIFICACION DE ORIGEN ---")
if planeta.lower() == "marte":
    print("Especie: Marciano. Piel roja.")
elif planeta.lower() == "venus":
    print("Especie: Venusiano. Alta temperatura.")
elif planeta.lower() == "jupiter":
    print("Especie: Joviano. Gasoso y gigante.")
else:
    print("Especie: Desconocida. Origen no catalogado.")

# 4. MATCH CASE
print("\n=== MENU DE ACCIONES ===")
print("1. Establecer comunicacion")
print("2. Analizar la nave")
print("3. Enviar mensaje de paz")
print("4. Finalizar contacto")

accion = int(input("Elige una accion (1-4): "))

match accion:
    case 1:
        print("Abriendo canal de comunicacion...")
    case 2:
        print("Escaneando tecnologia de la nave...")
    case 3:
        print("Transmitiendo: 'Venimos en paz'...")
    case 4:
        print("Contacto finalizado. Cerrando comunicacion.")

    case _:
        print("ERROR: Accion no valida.")
