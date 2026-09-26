# 1. solicitar al usuario que ingrese los siguientes datos:
#    nombre, edad, altura y si es estudiante o no.
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura en metros: ")
estudiante = input("¿Es estudiante? (sí/no): ")

# 2. convvertir los datos a tipos correctos

edad = int(edad)
altura = float(altura)

# 3. imprima todos los datos en pantalla usando formato de texto (f-strings)

print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print("El usuario es estudiante.") if estudiante == 'sí' else print("El usuario no es estudiante.")

# 4. la altura debe mostrarse con dos decimales

print(f"Altura: {altura:.2f} metros")
