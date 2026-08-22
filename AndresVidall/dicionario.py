pollo = {
    'peso':250,
    'raza' : 'covv500',
    'nombre': 'Roster',
    'lote': 15,
    'es_macho': True
}
pollo1 = {
    'peso':250,
    'raza' : 'covv500',
    'nombre': 'Rosita',
    'lote': 15,
    'es_macho': False
}


print(type(pollo))
print((pollo))
print((pollo1))

# obtener claves
print(pollo1.keys())
print(list(pollo.values())[2])
print(pollo1.items())

print(pollo1)
pollo1['es_macho'] = 'es machoo con pollo'
print(pollo1)