#Dar la Bienvenida
print("Bienvenido")
print("Vamos a calcular tu promedio")

#Datos Usuario
Lunes = float(input("Horas Lunes: "))
Martes = float(input("Horas Martes: "))
Miércoles = float(input("Horas Miércoles: "))
Jueves = float(input("Horas Jueves: "))
Viernes = float(input("Horas Viernes: "))
Sábado = float(input("Horas Sábado: "))
Domingo = float(input("Horas Domingo: "))

#Promedio
promedio = (Lunes + Martes + Miércoles + Jueves + Viernes + Sábado + Domingo) / 7
print("")
print("Promedio Semanal:", promedio)