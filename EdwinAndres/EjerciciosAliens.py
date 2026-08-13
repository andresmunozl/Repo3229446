planeta = input("¿Cual es su planeta de origen?: ")
nivel_amenaza = int(input("Ingrese su nivel de amenaza (1-10): "))
nivel_tecnologia = int(input("Ingrese su nivel de tecnología (1-10): "))

if nivel_tecnologia >= 5 and nivel_tecnologia <= 7:
    print(
        "Su nivel de tecnología funciona para tener comunicación "
        "y no es un peligro para la humanidad"
    )

if nivel_amenaza >= 1 and nivel_amenaza <= 5:
    print(
        "Su nivel de amenaza es bajo, no representa un peligro "
        "para la humanidad"
    )
else:
    print(
        "Su nivel de amenaza es alto, representa un peligro "
        "para la humanidad"
    )

if planeta == "mercurio":
    print("Su planeta de origen es Mercurio, el planeta mas cercano al sol")
elif planeta == "venus":
    print("Su planeta de origen es Venus, el planeta mas caliente del sistema")
elif planeta == "marte":
    print("Su planeta de origen es Marte, el planeta rojo del sistema")
else:
    print("Su planeta de origen no está en nuestra base de datos")

print("¿Que acción desea realizar?")
print("1. Establecer comunicación")
print("2. Analizar la nave")
print("3. Enviar mensaje de paz")
print("4. Finalizar contacto")

accion = int(input("Ingrese el número de la acción que desea realizar: "))

match accion:
    case 1:
        print("Estableciendo comunicación con la nave...")
    case 2:
        print("Analizando la nave...")
    case 3:
        print("Enviando mensaje de paz a la nave...")
    case 4:
        print("Finalizando contacto con la nave...")
    case _:
        print("Acción no válida")
