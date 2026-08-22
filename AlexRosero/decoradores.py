def multiplicar_por_dos(numero):
    return numero * 2

def aplicar_operacion(funcion, valor):
    return funcion(valor)

resultado = aplicar_operacion(multiplicar_por_dos, 5)
print(resultado)


def requier_auth(func):
    def wrapper(user):

        if user.lower() == "admin":
            return func(user)

        else:
            return "acceso denegado"
        
    return wrapper

def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"
auth_view_dashboard = requier_auth(admin_dashboard)

print(auth_view_dashboard("Admin"))
print(auth_view_dashboard("Invitado"))