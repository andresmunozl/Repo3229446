
print(" SIMULACIÓN DE PRIMER CONTACTO EXTRATERRESTRE")

nivel_tecnologia = int(input("nivel tecnologico de la nave de 1/10"))
if nivel_tecnologia >= 7:
    print("La tecnologia de la nave es suficientemente avanzada")
nivel_amenaza = int(input("Ingrese el nivel de amenaza  (1-10): "))
if nivel_amenaza <= 3:
    print("El extraterrestre puede ingresar a la nave humana")
else:
    print("El extraterrestre no puede ingresar a la nave humana")
planeta_origen = input("planeta de origen (marte/jupiter/neptuno/otro): ")
if planeta_origen == "marte":
    print("El extraterrestre es de marte")
elif planeta_origen == "jupiter":
    print("El extraterrestre es de jupiter")
elif planeta_origen == "neptuno":
    print("El extraterrestre es de neptuno")
else:
    print("Desconocido")
print("Seleccione una accion:")
print("1. Establecer comunicación")
print("2. Analizar la nave")
print("3. Enviar un mensaje de paz")
print("4. Finalizar el contacto")

accion = int(input("Ingrese el numero de la accion a realizar: "))

match accion:
    case 1:
        print("Estableciendo comunicación con el extraterrestre")
    case 2:
        print("Analizando la nave del extraterrestre")
    case 3:
        print("Enviando un mensaje de paz al extraterrestre")
    case 4:
        print("Finalizando el contacto con el extraterrestre")
    case _:
        print("Opcion no valida")

print(" FIN DE LA SIMULACION")