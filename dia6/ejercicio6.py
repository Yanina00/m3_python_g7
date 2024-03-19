"""
con dicional IF , si se cumple la condicion se ejecuta  el codigo 
if confidcion: codigo a ejecutar si es verdadero
 ELIF: es hibrido y se puede jecutar las veces que se desea su no se ejecuta el IF pasa al ELIF y si tampoco se ejecuta por 
 defaul pasa al ELSE
ELSE: si la condicion IF no se cumple else se ejecuta


    """
edad = int(input("ingrese su edad \n"))
if edad >= 18:
    print("eres mayor de edad ")  #el print despues del if debe tener 4 espacios de tabulacion
else: 
    print("eres menor de edad ")
    
    

if edad ==0:
    print('Este número es cero')
elif edad % 2 == 0:
    print('Este es un número par')
else:
    print('Este es un número impar')  
    
print("fin del programa")

