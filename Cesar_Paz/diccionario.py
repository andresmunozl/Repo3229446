pollo1 = {
    'raza': "chirapo",
    'peso': 2,
    'nombre': "roster",
    'lote': 18,
    'es_macho': True
}
pollo2 = {
    'raza': "covv500",
    'peso': 2.5,
    'nombre': "rosa",
    'lote': 15,
    'es_macho': False
}


print(type(pollo1))
print(pollo1.keys())

print(pollo1)
pollo1['nombre_padre'] = "pollo padre"
print(pollo1)