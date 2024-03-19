import random


# crear un programa de juego de piedra, papel o tijera

opciones = ["piedra", "papel", "tijera"]
juego_pc = random.choice(opciones)
#print(juego_pc)

while True:
 juego_usuario = input("ingrese juego cachipun  (Debe ser piedra, papel o tijera.): ").lower()
 if juego_usuario in opciones: 
     break
 else : 
     print("opcion no valida")
     
print(f"el usuario jugó {juego_usuario} y la computadora jugó {juego_pc}")
 
 
if juego_pc == juego_usuario: 
    print("Empate!")
elif (juego_usuario == "piedra" and juego_pc == "tijera") or \
     ( juego_usuario == "tijera" and juego_pc =="papel" ) or \
     (juego_usuario == "papel" and juego_pc == "piedra"): 
   print("Ganaste!!!")  
else :
    print("Perdiste!")
    