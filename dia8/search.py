"""import sys,random

buscar = int(sys.argv[1])  #numero a buscar

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) # .shuffle permite desordenar la lista, esye desorden es permanente
print(lista)

for posicion, numero in enumerate(lista):
    
    if buscar == numero:
        print("numero encontrado")
        break
    else:
        print(f"el numero {buscar} no se encontro en la posicion{posicion} ")
 
print("fuera del for") 
print(f"El numero {buscar} se encontro en la posición {posicion}")"""

from string import ascii_lowercase

contraseña = input("Ingrese la contraseña de 4 letras: ").lower()

caracteres = ascii_lowercase

for letra1 in caracteres:
    for letra2 in caracteres:
        for letra3 in caracteres:
            for letra4 in caracteres:
                intento = letra1 + letra2 + letra3 + letra4
                if intento == contraseña:
                    print(f"Contraseña encontrada: {intento}")
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("Contraseña no encontrada.")