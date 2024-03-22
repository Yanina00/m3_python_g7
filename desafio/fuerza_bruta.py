from string import ascii_lowercase

contraseña = input("ingrese su contraseña: ").lower()

caracteres = ascii_lowercase

contador = 0

#gato
#abcdefghijklmnopqrstuvwxyz
#7+1+21+14=43
for caracter in contraseña:
    print(caracter)
    for letra in caracteres:
        contador+=1
        if caracter == letra:
            break

print(f" La contraseña fue forzada en {contador} intentos")