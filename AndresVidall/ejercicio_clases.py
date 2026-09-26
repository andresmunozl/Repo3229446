cars = {
    'nombre': 'Macqueen',
    'color':  'rojo',
    'lugar_carrera' : (1.93545457, 2.15454125, 3.15458421, 4.01247854),
    'prlicula': 'Cars',
    'copas_piston': True,
    'mejores_amigos': ['Two Mater', 'Mack'],
    'personajes' : {
        'novia' : 'Saly',
        'Frase' : '"Soy más rápido que rápido.  Más rápido que rápido. ¡Soy un rayo!"'
    }
}

# imprimir el dicionari
print(type(cars))
print((cars))

#imprimir la posicio
print(list(cars.values())[1])

# imprimir tupl 
print(type('lugar_carrera'))

print('lugar_carrera'[-0])