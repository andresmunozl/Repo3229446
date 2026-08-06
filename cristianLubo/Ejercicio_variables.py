# punto1
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura en metros: ")
estudiante = input("Es estudiante (si o no): ")

# punto2
nombre = str(nombre)
edad = int(edad)
altura = float(altura)
estudiante = bool(estudiante)

# punto3
print(f"nombre: {nombre}")
print(f"edad: {edad}")
print(f"altura: {altura:.2f}")
print(f"estudiante: {estudiante}")