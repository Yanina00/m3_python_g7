"""
while condición:
# código a implementar
    """
"""
import getpass

password = getpass.getpass("i grese su contraseña:\n")
# En este caso definimos nuestro password como "hola mundo"
# En este caso, mientras la contraseña no sea hola mundo,
# seguirá solicitando la contraseña, pero esta vez con otro mensaje.

while password != "hola mundo":
 password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez.")
 
 print("Clave Correcta. Puedes utilizar tu programa")
# Posterior a esto podríamos agregar el código de nuestro programa.

"""   
#Iteracionde n veces
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i = i + 1 #incremento en 1
    
print("fuera del while")

#ifegtrh
i = 1
while i <= 10:
    print(f"El valor de i es: {i}")
    i = i + 2 #incremento en 1
    
print("fuera del while")
 
 #multiplicamos por 2, i=*2 es igual a  i*=2

i = 1
while i <= 10:
    print(f"El valor de i es: {i}")
    i *= 2 #incremento en 1
    
print("fuera del while")


saludo = "hola"
saludo += " mundo"
print(saludo) # hola mundo
saludo += "chao"
print(saludo) # hola mundo chao

i = 1 # primer valor a sumar
suma = 0
while i <= 100:
 suma += i # acumulamos para la suma
 i += 1 # incrementamos para sumar el siguiente valor

print(f"El resultado final es {suma}")
