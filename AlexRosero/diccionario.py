pollo1 = {

    'peso': 250,
    'raza': 'covv500',
    'nombre': 'Roster',
    'lote': 15,
    'es_macho': True,
    'colores': ['azul', 'rojo']


}
pollo2 = {

    'peso': 250,
    'raza': 'covv500',
    'nombre': 'Roster',
    'lote': 15,
    'es_macho': False


}

print(type(pollo1))
print(pollo1)

print(pollo1.keys())
print(pollo1.values())
print(pollo1.items())

print(pollo1)
pollo1["es_macho"] = "es_machoclaro que si"
print(pollo1)