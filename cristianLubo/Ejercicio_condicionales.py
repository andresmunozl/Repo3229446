# punto 1 (condicional simple)
nivel_tecnologia = int(input("Ingrese el nivel de tecnologia de la nave (1-10): "))
if nivel_tecnologia >= 7:
    print("La tecnologia de la nave es suficientemenete avanzada para establecer comunicacion")

#punto 2 (condicional compuesto)
nivel_amenaza = int(input("Ingrese el nivel de amenaza del extraterrestre (1-10): "))
if nivel_amenaza <= 3:
    print("El extreterrestre puede ingresar a la nave humana")
else:
    print("el extraterrestre no puede ingresar a la nave humana")

# punto 3 (condicional multiple)    
planeta_origen = input("Ingrese el planeta de origen (marte/jupiter/neptuno/otro): ")
if planeta_origen == "marte":
    print("El extraterrestre es de marte")
elif planeta_origen == "jupiter":
    print("El extraterrestre es de jupiter")
elif planeta_origen == "neptuno":
    print("El extraterrestre es de neptuno")
else:
    print("Desconocido")

# punto 4 (match case)
print("seleccione una accion:")
print("1. Establecer comunicación")   
print("2. Analizar la nave")   
print("3. Enviar un mensaje de paz")   
print("4. Finalizar el contacto")   

accion = int(input("Ingrese el numero de la accion a realizar"))

match accion:
    case 1:
        print("Estableciendo comunicación con el extraterrestre...")
    case 2:
        print("Analizando la nave del extraterrestre...")
    case 3:
        print("Enviando un mensaje de paz al extraterrestre...")
    case 4:
        print("Finalizando el contacto con el extraterrestre...")
    case _:
        print("Opcion no valida.")

