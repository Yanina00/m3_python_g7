

cantidad_notas = int(input("ingrese camtidad de notas "))
i = 0 # 0,1,2
suma_notas = 0
while i< cantidad_notas:
    nota = float(input("Ingresa tu nota: "))
    suma_notas = suma_notas + nota
    i += 1

print(f"el promedio de notas es: {round(suma_notas/cantidad_notas,2)}")