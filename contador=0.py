contador=1
while contador<3:
    print("Contador",contador)
    contador +=1
else: 
    print("El bucle finalizo")
    
    
while True:
    print("Este bucle finalizo")
    break


procesocompra= True

while procesocompra: 
    entrada= input("Escribe 'salir' para detener: ")
    if entrada == "salir":
        procesocompra= False
        print("Ok, ADIOS")
    else:
        print("Haz ingresado:", entrada)
        
        
i=0
j=0
k=0
while i<=3:
    i=1
    j=1
    k=1
    while j<=3:
        print(f"i={i}, j={j}, k={k}")
        break