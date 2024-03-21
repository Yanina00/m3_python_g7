import sys, time

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

i = int(sys.argv[1]) # fijar valor inicial ['dia7/bomba.py', '10'] crea una lista, al poner la carpeta archivo y el 10

while i > 0:
    print(f"el valor de i {i}")
    time.sleep(1) #tiempo de espera 3 segundos  , para ocupar el tiempo importamos time si ya tenemos importado algo solo añadimos una coma y el time
    i -= 1 # decremento en 1 numero(restando1)
    
print("BOOOMMMMMM!!!")    