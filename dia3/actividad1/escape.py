
import  math

#calculando la velocidad de escape 
radio=float(input("Ingrese el radio del planeta en metros: "))
gravedad=float(input("Ingrese la constante gravitacional: ""m/s^2"))
velocidad_escape=math.sqrt(2 * radio * gravedad)
print=(f"la velocidad del escape es:{velocidad_escape} m/s" )
