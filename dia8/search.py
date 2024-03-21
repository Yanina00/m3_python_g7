import sys,random

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
print(f"El numero {buscar} se encontro en la posición {posicion}")