# Paso 1: Pedir los datos al usuario
nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura en metros (ej: 1.70): "))
es_estudiante = input("¿Es estudiante? (Si/No): ")

# paso 2 convertir datos
es_estudiante = es_estudiante == "Si"

# paso 3 Imprima todos los datos en pantalla 

print(f"\n--- Datos del Usuario ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} metros")
print(f"Estudiante: {es_estudiante}")

