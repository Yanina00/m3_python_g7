
#generar los 10 primeros números pares yalmacenarlos en una lista:

n = 10
lista_pares = [] #lista vacia, 0 elementos
for i in range(n): 
    lista_pares.append(2*i + 2)
    
lista_pares2 = [2*i + 2 for i in range(n)] #comprehesions
print(lista_pares)
print(lista_pares2)    


valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
   if valor % 2 == 0:
    divisibles.append('Divisible')
   else:
    divisibles.append('No Divisible')
    
print(divisibles)

#si convertimos el código anterior en List comprehension queda de la siguiente manera:

divisible2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]   
print(divisible2)

##FILTRAR
lista = ['Lechugas', 'Tomates', 5, 10,True, False, True, 'Papas',5.1, 45.2, 1, 2, 0]
lista_str= []
lista_int= []
count_str = 0

for elemento in lista:
   if type(elemento) is str:
     count_str += 1
     lista_str.append(elemento)
   elif type(elemento) is int:
        lista_int.append(elemento)
print(count_str)
print(lista_str)
print(lista_int)

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))
print((lst_str))

##DICCIONARIO COMPREHESIONS
claves = ['nombre' ,'apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = {k:v  for k,v   in zip(claves, valores )}
print(diccionario2)