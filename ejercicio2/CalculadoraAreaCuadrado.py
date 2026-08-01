
class CalculadoraAreaCuadrado:
    
    
    def __init__(self, lado):
        
        # VALIDACIÓN DE DATOS Y MANEJO DE ERRORES:
        # 1. Comprobamos que 'lado' sea un número (entero o flotante).
        # isinstance(lado, (int, float)) devuelve True si lado es int o float.
        if not isinstance(lado, (int, float)) or isinstance(lado, bool):
            # TypeError se lanza cuando el TIPO de dato es incorrecto.
            raise TypeError("Error: El valor del lado debe ser un número (entero o decimal).")
        
        # 2. Comprobamos que el número sea estrictamente mayor a cero.
        if lado <= 0:
            # ValueError se lanza cuando el TIPO es correcto pero el VALOR no es válido.
            raise ValueError("Error: El lado del cuadrado debe ser un número positivo mayor que cero.")
        
        # Si pasa las validaciones, asignamos el valor al atributo interno 'lado'.
        self.lado = lado

    # Método para calcular el área del cuadrado
    def calcularArea(self):
        # El área de un cuadrado es lado multiplicado por lado (o lado al cuadrado).
        return self.lado * self.lado

    # Método para calcular el perímetro del cuadrado
    def calcularPerimetro(self):
        # El perímetro de un cuadrado es la suma de sus 4 lados (lado * 4).
        return self.lado * 4
    ## Clase CalculadoraAreaCuadrado: AAtributo lado. Métodos para calcularArea() () y calcularPerimetro(). 
    # Bloque de ejecución principal
if __name__ == "__main__":
    try:
        # 1. Creamos un objeto de la clase indicando que el lado mide 5 unidades.
        mi_cuadrado = CalculadoraAreaCuadrado(5)
        
        # 2. Llamamos a los métodos y guardamos sus resultados en variables.
        area_calculada = mi_cuadrado.calcularArea()
        perimetro_calculado = mi_cuadrado.calcularPerimetro()
        
        # 3. Imprimimos los resultados en la consola.
        print(f"--- RESULTADOS DEL CUADRADO ---")
        print(f"Medida del lado: {mi_cuadrado.lado}")
        print(f"Área del cuadrado: {area_calculada}")
        print(f"Perímetro del cuadrado: {perimetro_calculado}")
        
    except (ValueError, TypeError) as error:
        # Capturamos los errores de validación si ingresamos datos inválidos
        print(error)