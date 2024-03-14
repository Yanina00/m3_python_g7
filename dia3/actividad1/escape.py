
import  math

#calculando la velocidad de escape 
radio1=float(input("Ingrese el radio del planeta en km: "))
gravedad=float(input("Ingrese la constante gravitacional en m/s^2: "))
radio2=float(radio1 * 1000)
velocidad_escape=math.sqrt(2 * radio2 * gravedad)

print(f"la velocidad del escape es:{round(velocidad_escape,1)} m/s" )
