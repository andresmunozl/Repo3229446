def require_auth(func):
    def wraper(user):
        if user == "admin":
            return func(user)
        else:
            return "Aceso denegado"
    return wraper

@require_auth
def admin_dashboard (user):
    return f"bienvenido al paner care chimba, {user}"

print(admin_dashboard("Admin"))