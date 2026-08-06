# 1. Solicitar datos
Nombre = input("Ingrese su nombre: ")
Edad = input("Ingrese su edad: ")
Estatura = input("Ingrese su estatura: ")
Estudiante = input("¿Es estudiante? (s/n)")

# 2. Convertir
Nombre = str(Nombre)
Edad = int(Edad)
Estatura = float(Estatura)
Estudiante = bool(Estudiante)

# 3. imprimir 
print(f"Nombre: {Nombre}, Edad: {Edad}, Estatura: {Estatura:.2f}m, ¿Es estudiante? {Estudiante}")