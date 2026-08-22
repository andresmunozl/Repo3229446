#def multiplicar_por_dos(num):
 #   return num * 2 

#def aplicar_operacion (funcion, valor):
 #   return funcion(valor)

#resultado = aplicar_operacion(multiplicar_por_dos, 5)
#print(resultado)

def requiereAuth(func):
    def wraper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso demegado"

    return wraper

def admin_dashboard (user):
    return f"bienvenidos a nimalayaa", {user}

auth_view_dashboar = requiereAuth(admin_dashboard)


print(auth_view_dashboar("admin"))
print(auth_view_dashboar("Invitado"))