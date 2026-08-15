pollo = {
    'peso': 250,
    'edad': 'cobb 500',
    'nombre': 'Caldo',
    'lote': 2,
    'es_macho': False
}
print(type(pollo))
print(pollo)

pollo2 = {
    'peso': 350,
    'edad': 'Ross 308',
    'nombre': 'Cofi',
    'lote': 2,
    'es_macho': True
}
print(type(pollo2))
print(pollo2)

print(pollo.keys())
print(pollo.values())
print(pollo.items())

print(pollo)
pollo['enfermedades'] = 'Bronquitis'
print(pollo)
