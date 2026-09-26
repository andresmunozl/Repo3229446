# def multiplicar_por_dos(numero):
#     return numero * 2


# def aplicar_operacion(funcion, valor):
#     return funcion(valor)


# resultado = aplicar_operacion(multiplicar_por_dos, 5)
# print(resultado)


def require_auth(func):
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "acceso denegadooooooo"

    return wrapper


def admin_dashboard(user):
    return f'bienvenido al panel de {user}'


auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard('Admin'))
print(auth_view_dashboard('Invitado'))
