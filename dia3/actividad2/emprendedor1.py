
precio_suscripcion=int(input("ingrese precio de suscripcion: "))
numero_usuario=int(input("ingrese cantidad de usuario: "))
gastos_totales:float(input("ingrese gastos totales: "))
utilidades= calcular_utilidades (precio_suscripcion, numero_usuario, gastos_totales)
print(f"las utilidades del proyecto son :{utilidades}")