from ast import Import
#Ejercicio de elevador


#Consideraciones:
#Ejemplo de impresión en consola
#Arreglo de pisos: [5, 29, 13, 10]
#Piso inicial de ejecución: 4
#Pisos ingresados: {5:2, 29: 10, 13: 1, 10:1}
#Sentido: Subiendo

#--------------------------------------------------------------------------------------------------------------

#Constructor de arreglos, arreglo inicial y arreglo para los pisos ingresados

arregloInicialPisos = [5,29,10,13] #Arreglo de pisos iniciales 
pisos = [] 

#______________________________________________________________________________________________________________
#Determinar si el piso en que se encuentra el elavador corresponde al arreglo de pisos o no para eliminarlo o no
def verificar_piso_arreglo(pisos, arregloInicialPisos):

    contador = 0
    pisoEnArreglo = False
    while pisoEnArreglo == False:
        for _ in arregloInicialPisos: #Cualquier dato

            if pisos == arregloInicialPisos[contador]:
                pisoEnArreglo = True
                break
            contador += 1

        if pisoEnArreglo == False:
            break

    return pisoEnArreglo

#______________________________________________________________________________________________________________
def llenar_arreglo_pisos():
    for n in range(1, 30, 1): #Rango de pisos y se define el aumento o la disminucion de los mismos de uno en uno
        pisos.append(n)

#______________________________________________________________________________________________________________
#Pedir un nuevo piso para agregarlo a la cola de arreglos
def nuevo_piso(arregloInicialPisos):

    pisoNuevo = True
    while pisoNuevo:  #Condicional para verificar si se ingresa un nuevo piso a la cola del arreglo o no
        
        opc= input ("\n¿Desea pedir un piso nuevo? Si o No (s/n) ----> ")

        if opc == "s" or opc == "S" :
            print('Diigite el numero del piso: ')
            arregloInicialPisos.append(int(input()))
            break
        else:
            pisoNuevo = False
        
#______________________________________________________________________________________________________________
#Eliminar un piso  de la cola de arreglos
def eliminar_cola_pisos(pisos, arregloInicialPisos):

    arregloInicialPisos.remove(pisos)

#______________________________________________________________________________________________________________
#Metodo para mover el elevador
def mover_elevador(pisoActual, elevador, pisosIngresados):

    if len(pisosIngresados) == 0:
        nuevo_piso(pisosIngresados)
        
    while len(pisosIngresados) != 0:  #Condicional mientras los pisos sean diferentes de 0 

        print('Elevador en piso ', elevador[pisoActual-1])
        pisoPedido = pisosIngresados[0]

        if elevador[pisoActual-1] < pisoPedido:

            print('Elevador Subiendo')
            pisoActual += 1

        if elevador[pisoActual-1] > pisoPedido:

            print('Elevador Bajando')
            pisoActual -= 1

        while verificar_piso_arreglo(pisoActual, pisosIngresados): 

            eliminar_cola_pisos(elevador[pisoActual-1], pisosIngresados) #Eliminar del arreglo el piso ya alcanzado 
            print('Elevador se detiene --->', arregloInicialPisos) #Arreglo nuevo
            nuevo_piso(pisosIngresados)
            break

#______________________________________________________________________________________________________________
#Llamado de metodos para iniciar
llenar_arreglo_pisos()
mover_elevador(4, pisos, arregloInicialPisos)