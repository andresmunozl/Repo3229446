donaciones = ['enlatados', 'granos', 'agua', 'ropa']
print(type(donaciones))

print(donaciones)
donaciones.append('medicinas')
print(donaciones)
donaciones.append('medicinas')
donaciones.remove('medicinas')
donaciones.sort(reverse=True)
print(donaciones)
print(donaciones.count('medicinas'))
