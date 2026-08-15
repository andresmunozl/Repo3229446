nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros ejm: 1.70):"))

estudiante = input("¿Es estudiante? (SI o NO): ")

es_estudiante = estudiante.lower() == "SI"

print(f"\n--- Datos del Usuario ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} metros")
print(f"Estudiante: {es_estudiante}")
