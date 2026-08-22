donaciones = ['enlatados', 'granos', 'agua', 'ropa']
print(type(donaciones))

print(donaciones)
donaciones.append('medicinas')
donaciones.sort(reverse=False)
print(donaciones)
donaciones.append('camas')
print(donaciones)
donaciones.remove('camas')
print(donaciones)
donaciones.append('cobijas')
print(donaciones)
print(donaciones.count('medicinas'))

