nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
altura = float(input("ingrese su altura ('ejemplo 1.70'): "))
estudiante_respuesta = input("es estudiante (si/no): ").strip().lower()
es_estudiante = estudiante_respuesta == "si"

# imprimir los datos

print(f"nombre:  {nombre}, edad:  {edad}, altura: {altura:.2f}, es estudiante:  {es_estudiante}" )

