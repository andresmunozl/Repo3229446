print('Hola')

nombre_user = input('Ingrese su nombre: ')
rol_user = input('¿usted es estudiante o profesor?: ')
edad_user = input('Ingrese su edad: ')
altura_user = input('Ingrese su altura: ')

nombre = str(nombre_user)
rol = bool(rol_user == 'estudiante')
edad = int(edad_user)
altura = float(altura_user)


print(f"Bienvenido {rol}, {nombre}, de edad {edad}, y altura de {altura}")
