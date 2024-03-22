

#primeros auxilios

usuario = input("¿Responde a estimulos? ").lower()
if usuario == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    exit()
elif usuario == "no":
    print("Abrir via aerea")
    
paso1 = input("¿Respira? ").lower()   
if paso1 == "si":
    print("permitirle posicion de suficiente ventilacion")
    exit()
elif paso1 == "no":
    print("Administrar 5 Ventilaciones y llamar a Ambulancia")
    
while True:    
   paso2 = input("¿Signos de Vida? ")
   if paso2 == "si":
        print("Reevaluar a la espera de la Ambulancia")  
       
   elif paso2 == "no":
        print("Administrar Compresiones Torácicas hasta que llegue la ambulancia ")
   paso3 = input("¿Llegó la Ambulancia? ").lower()
   if paso3 == "si":
        exit()
        
    
    
     
    
    
    
