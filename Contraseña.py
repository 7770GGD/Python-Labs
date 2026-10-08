contraseña = ""
while contraseña != "1234":
    contraseña = input("Ingrese la contraseña: ")
    if contraseña != "1234":
        print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("Contraseña correcta. Acceso concedido.")