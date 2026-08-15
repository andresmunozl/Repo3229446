donaciones = ['enlatados','granos','agua','ropa', ]
print(type(donaciones))


print(donaciones)
donaciones.append('medicinas')
print(donaciones)
donaciones.append('medicinas')
donaciones.sort(reverse=False)
donaciones.remove('medicinas')
print(donaciones)
print(donaciones.count('medicinas'))
