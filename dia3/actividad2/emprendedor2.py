#el emprendedor considera 2 tipos de usuarios diferenciados,
#los usuarios normales y los usuarios premium a los cuales se les cobrará una
#suscripción un 50% mayor.

precio_suscripcion=float(input("ingrese precio de suscripcion: "))
numero_usuario=int(input("ingrese cantidad de usuario: "))
numero_usuario_premium=int(input("ingrese la cantidad ed ususario premium: "))
gastos_totales=float(input("ingrese gastos totales: "))
utilidades=((precio_suscripcion * numero_usuario) +(precio_suscripcion * 1.5 * precio_suscripcion) - gastos_totales)

print(f"las utilidades del proyecto son :{utilidades}")