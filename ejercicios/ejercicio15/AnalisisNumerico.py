## Clase AnalisisNumerico: Atributo numero. Métodos para esPar() (retorna verdadero/falso) y obtenerDoble().


class AnalisisNumerico:

    def __init__(self, numero):
        self.numero = numero

    def esPar(self):
        esPar = self.numero % 2 == 0
        return esPar

    def obtenerDoble(self):

        return self.numero * 2


a = AnalisisNumerico(8)
print(a.esPar())
print(a.obtenerDoble())

