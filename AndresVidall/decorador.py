def decorador (funcion_original):
    def wrapper (*arg, **kwargs):
        print("esto se imprime antes de ejecuatar la funcion")

        resultado = funcion_original(*arg, **kwargs)

        print (" esto se imprime despues de ejecutar la funcion")
        return(resultado)
    return wrapper
@decorador
def saludar (nombre):
    print(f"hola, {nombre}, espero se encuentre bien")
    return "saludo completado"

saludar("Andres")