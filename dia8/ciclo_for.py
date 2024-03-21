"""
CICLO FOR
for variable in iterable
    """
    
    # Con un sólo valor [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    print(i)
 
print("******")    
# Con dos valores   [4,5,6,7,8,9]
for i in range(4,10):  #en primer  valor si se considera , el ultimo valor no se considera
   print(i)    
   
print("********")   

# Con tres valores  [4,6,8]
for i in range(4,10,2):  #el valor de inicio que se considera, el valor de termino que no se considera
   print(i)              #, y el tercer valor "2" es el incremento (+2)
   
   
""" FOR EN JAVASCRIPT
for (let i = 4; i < 10; i++) {
    console.log(i);
}   """ 

print("******")
#LISTAS
a = [2,"4",True,3,"5"]
for elemento in a:
  print(elemento)
  
print("******")
#string   --> son similares a las listas
texto = "hola mundo"
for caracter in texto:
   print(caracter)
   
#DICCIONARIO

datos_personales = {"Nombre": "Carlos",
              "Apellido": "Santana",
              "Edad": "30"}  

for clave in datos_personales:   #aqui se obtienen las claves que con nombre,apellido,edad
   print(clave)
print("******") 
for clave in datos_personales:
   print(datos_personales[clave])   #aqui obteneos los datos personales d elas claves(valor)

print("******") 

for clave,valor in datos_personales.items():
   print(f"clave: {clave} - valor:{valor}")


#ENUMERATE

print("******") 

for posicion, caracter in enumerate(texto):
    print(f"La posición {posicion} del caracter {caracter}")
    
print("******") 
    
for posicion, numero in enumerate(a):
    print(f"La posición {posicion} del caracter {numero}")    


print("******") 

#ZIP unir varios iterables

prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
  print(f'{p} {fruta} es de color {color}')
  
print("******") 
#breack

numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]  
for numero in numeros:
   print(numero)
   if numero ==3:
       break                #solo imprime 2,4,true y 3 por que llega hasta el 3 y sale del ciclo
   