nombre = (input("Ingrese su nombre: "))
edad = (input("Ingrese su edad: "))
altura = (input("Ingrese su altura en metros: "))
es_estudiante = (input("¿Es estudiante? (True/False): "))

nombre = str(nombre)
edad = int(edad)        
altura = float(altura)
es_estudiante = bool(es_estudiante)

print(f"El nombre es: {nombre}, tiene una edad de: {edad}, su altura es: {altura:.2f}, es estudiante: {es_estudiante}")

