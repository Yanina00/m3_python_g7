
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
  if a[i] >= 1000:
   filtered_array.append(a[i]) 
   #[expresión for variable in iterable if condición ]
    #siguiendo la logica 
filtrado_numeros = [a[i]  for i in range(n) if a[i] >= 1000] #se utiliza la tercera expresion de comprehesion
#si el if esta antes del for, DEBE haber un else
#si solo hau 1 if, va despues de for in range(n)
print(filtrado_numeros)

print(filtered_array)




