# punto 1
nombre = input("ingrese su nombre :")
edad = input("ingrese su edad :")
altura = input("ingrese su altura :")
eres_estudiante = input("eres estudiante ¿si o no? :")

# punto 2
nombre = str(nombre)
edad = int(edad)
altura = float(altura)
eres_estudiante = bool(eres_estudiante)

# punto 3

print(f"nombre: {nombre}")
print(f"edad: {edad}")
print(f"altura: {altura:.2f} ")
print(f"eres_estudiante: {eres_estudiante}")
