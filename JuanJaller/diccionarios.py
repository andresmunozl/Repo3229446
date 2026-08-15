pollo1 = {
    'peso': 250,
    'raza': 'covv500',
    'nombre': 'Roster',
    'lote': '15',
    'es_macho': True 
}
pollo2 = {
    'peso': 250,
    'raza': 'covv500',
    'nombre': 'hola',
    'lote': '15',
    'es_macho': True    
}
print(type(pollo1))
print(pollo1.keys())

print(pollo1)
pollo1['nombre_padre'] = 'Arnulfo'
print(pollo1)