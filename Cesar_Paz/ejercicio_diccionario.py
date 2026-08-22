discografia = {
    'nombre_banda': 'metallica',
    'año_formacion': 1981,
    'numero_integrantes': 4,
    'aun_giras': True,
    'nombre_album': ['kill em all', '...And justice for all', 'master of puppets', 'ride the lightning', 'nothing else matters']
}

print(type(discografia))
print(discografia.keys())
print(discografia)
print(discografia['nombre_album'][1])
discografia['nombre_album'].append('reload')
print(discografia)