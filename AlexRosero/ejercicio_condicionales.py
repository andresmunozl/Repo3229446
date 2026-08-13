




print ("==========================================================================")

print(                "Que tal este es el planeta tierra"              )

print ("==========================================================================")


print ("==========================================================================")
comunicacion = input("Cuentan con la tecnologia para comunicarse? (si/no): ")
print ("==========================================================================")

if comunicacion == "si":

    print ("==========================================================================")

    print(                "Bienvenidos ala Tierra"              )

    print ("==========================================================================")


print ("==========================================================================")
amenaza = input("son una ameza para la Tierra? (si/no): ")
print ("==========================================================================")

if amenaza == "no":

    print ("==========================================================================")

    print(                "Bienvenidos ala Tierra"              )

    print ("==========================================================================")    

else:

    print ("==========================================================================")

    print(                "Lo sentimos no pueden ingresar ala tierra"              )

    print ("==========================================================================")

    print ("==========================================================================")

    tipoextraterrestre=["humanoide","retiloide","insectoide"]

tipoextraterrestre = input("Ingrese el tipo de extraterrestre que es: ejemplo: humanoide, retiloide, insectoide: ")
     
if tipoextraterrestre == "humanoide":
        print ("==========================================================================")
        print(                "Bienvenidos ala Tierra"              )
        print ("==========================================================================")
elif tipoextraterrestre == "retiloide":
        print ("==========================================================================")    
        print(                "Bienvenidos ala Tierra"              )
        print ("==========================================================================")
else:
        print ("==========================================================================")    
        print(                "Lo sentimos no pueden ingresar ala Tierra"              )
        print ("==========================================================================")

opcion = int(input("Ingrese una opcion: " \
"1. Estrablecer comunicacion con la Tierra, " \
"2. Analizar la nave extraterrestre, " \
"3. Enviar un mensaje de paz ala Tierra, " \
"4. Finalizar contacto: "))

match  opcion:

    case 1: 
     print ("==========================================================================")
     print ("Estamos tratando de establecer comunicacion ")
     print ("==========================================================================")

    case 2:
        print ("==========================================================================")
        print ("vamos a pasar a analizar la nave")
        print ("==========================================================================")

    case 3:
        print ("==========================================================================")
        print ("cual sera el mensaje de paz")
        print ("==========================================================================")

    case 4:
        print ("==========================================================================")
        print ("el contacto a terminado ")
        print ("==========================================================================")