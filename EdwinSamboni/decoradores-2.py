def requiere_auth(func):
    def warpper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"
        
    return warpper

@requiere_auth
def admin_dashboard(user):
    return f"Bienvenido al papel, {user}"

print(admin_dashboard("Admin"))