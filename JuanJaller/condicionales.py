tecnologia = input("Nivel de tecnologia de la nave (baja/media/alta): ")
amenaza = input("Nivel de amenaza del extraterrestre (bajo/medio/alto): ")
planeta = input("Planeta de origen (marte/venus/jupiter/otro): ")

# Condicional simple
if tecnologia == "alta":
    print("La nave tiene tecnologia suficiente para establecer comunicacion.")

# Condicional compuesto
if amenaza == "bajo":
    print("El extraterrestre puede ingresar a la nave humana.")
else:
    print("El extraterrestre NO puede ingresar a la nave humana.")

# Condicional multiple
if planeta == "marte":
    print("Es un extraterrestre de tipo Marciano.")
elif planeta == "venus":
    print("Es un extraterrestre de tipo Venusiano.")
elif planeta == "jupiter":
    print("Es un extraterrestre de tipo Joviano.")
else:
    print("Es un extraterrestre de origen desconocido.")

# Match case
print("\nQue accion deseas tomar?")
print("1. Establecer comunicacion")
print("2. Analizar la nave")
print("3. Enviar un mensaje de paz")
print("4. Finalizar el contacto")

accion = input("Elige una opcion (1-4): ")

match accion:
    case "1":
        print("Estableciendo comunicacion con la nave extraterrestre...")
    case "2":
        print("Analizando la estructura y tecnologia de la nave...")
    case "3":
        print("Enviando mensaje de paz a la civilizacion...")
    case "4":
        print("Finalizando el contacto.")
    case _:
        print("Opcion no valida. Intenta con un numero del 1 al 4.")