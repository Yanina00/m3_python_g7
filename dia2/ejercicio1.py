print("dia 2 de ejercicios")

edad="44"

#duplicacion
print(10/20)
print(type(edad))
print(3*edad)
numero=100
print(type(numero))
print(3*(numero))
# metodo .count() y  len()
print("yaninabelmar".count("a"))
print(len("18.728.677-8")) #contar cuantos caracteres hay
 #print(len(123456789)) #TypeError: object of type 'int' has no len()

# metodo .upper()   .lower() .title()
print("kaKAtOtO".upper()) #todo en mayuscula
print("kaKAtOtO".lower()) #todo en minuscula
print("kaKAtOtO".title()) #la primera con mayuscula de cada palabra
#que opina del worldcoin para escanear tu iris

#metodo .join()
print("; ".join(["a","b","c"])) #es para separar string mediante el caracter 
#que este al inicio del parentesis en este caso mediante la coma y un espacio

#/n  salto en linea
print("hola\ncomo estan\ntodos")
print("hola\na\ntodos")

#tipos de datos
entero=8
decimal=2.5
cadena="esto es una cadena"
booleanos=True

print(type(entero)) #<class 'int'>
print(type(decimal)) #<class 'float'>
print(type(cadena)) #<class 'str'>
print(type(booleanos)) #<class 'bool'>

#cambiar la misma variable
numero2=500
numero2= numero2 + 500  # la variable numero2 ya no vale lo mismo del inicio se reafirma otro valor
print(numero2)


#precision de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {promedio:.2f}") 
print(f"resulta de la division {1/9:.4f}")  #:.3f y round()3   es para generar solo 3 decimales
print(f"resulta de la division {round(1/9,3)}")

#INGRESO DE DATOS (INPUT)

nombre=input("Ingrese su nombre: ")
print(nombre)
edad=input("Ingrese tu edad: ")
print(edad)
print(f"tu edad es {edad}")

#ejercicio guiado
nombre = input('Ingrese su Nombre: ')
edad = input('Ingrese Edad: ')
ocupacion = input('Ingrese Ocupación: ')
lugar = input('En dónde?: ')
caracteristica_1 = input('Ingrese 3 características:\n1. > ')
caracteristica_2 = input('2. > ')
caracteristica_3 = input('3. > ')
pasatiempo = input('Cuál es tu pasatiempo: ')
hacer = input('¿Que quieres hacer? ')

print(f'''
Mi nombre es {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar}.
Soy una persona {caracteristica_1}, {caracteristica_2} y {caracteristica_3}.
Mi pasatiempo es {pasatiempo} y me gustaría poder {hacer}.''')