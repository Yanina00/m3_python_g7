#Calculando IMC
#Ingresando datos

peso = float(input("ingrese su peso en Kg: "))

while True:
     altura_cm = float(input("ingrese su altura en centimetros: "))
     if altura_cm ==0:
         print("el valor no puede ser 0")
     else:
         break    

#ajustando valores de cm a m

altura_m = altura_cm / 100 

calculo_imc = peso/(altura_m**2)

print(f"Su IMC es {round(calculo_imc,2)} La clasificación OMS es: ",end="")

if calculo_imc < 18.5:
    print("Bajo peso")
elif 18.5 <= calculo_imc < 25:
    print("Adecuado")
elif 25 <= calculo_imc < 30:
    print("Sobrepeso")
elif 30 <= calculo_imc < 35:
    print("Obesidad Grado I")
elif 35 <= calculo_imc < 40:
    print("Obesidad Grado II")
else:
    print("Obesidad Grado III")