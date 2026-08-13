# Solicitud de datos
comunicacion   = input("¿Tienes forma de comunicarte? ")
nivel_amenaza  = input("¿Cual es su nivel de amenaza? ")
planeta_origen = input("Ingrese su planeta de origen: (júpiter/neptuno/otro¿Cual?)) ")

# 1. Condicional simple (if)
puede_comunicarse = False

if comunicacion == "sí":
    puede_comunicarse = True
    print("Nave con tecnología suficiente. Comunicación establecida.")

# 2. Condicional compuesto (if/else)
if nivel_amenaza == "bajo":
    puede_entrar = True
    print("Extraterrestre clasificado como no amenazante. Acceso permitido a la nave humana.")
else:
    puede_entrar = False
    print("Extraterrestre clasificado como amenazante. Acceso denegado.")

# 3. Condicional múltiple (if/elif/else)
if planeta_origen == "júpiter":
    tipo_extraterrestre = "pacífico"
    print("Clasificación: Extraterrestre pacífico de Júpiter.")
elif planeta_origen == "neptuno":
    tipo_extraterrestre = "neutral"
    print("Clasificación: Extraterrestre neutral de Neptuno.")
else:
    tipo_extraterrestre = "hostil"
    print("Clasificación: Extraterrestre potencialmente hostil.")

# 4. Match case para seleccionar acción

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