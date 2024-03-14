##calculando utilidades del proyecto comida de mascotas con utilidades anteriores


precio_suscripcion=float(input("ingrese precio de suscripcion: "))
numero_usuario=int(input("ingrese cantidad de usuario: "))
gastos_totales=float(input("ingrese gastos totales: "))
utilidades=(precio_suscripcion * numero_usuario - gastos_totales)
utilidades_anterior=float(input("ingrese las utilidades anteriores: "))

print(f"razon entre las utilidades actuales y anteriores del proyecto son :{round(utilidades/utilidades_anterior,2)}")
