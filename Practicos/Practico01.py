#lista con los datos Importantes de mi persona
lista = [['Nombres: Alvaro Sebastain'],
        ['Apellidos: Cepeda Choque'],
        ['CI: 10410410'],
        ['Telefono: 73354413'],
        ['Direccion: Vencete Donoso# 495']]
i = 0

salir = True

#Bucle del menu

while salir:

    #Interfaz simple del menu
    print("1) Mostrar Menu")
    print("2) Salir")
    # Primero se debe se ahcer un espacio para poder ingresar la opcion
    opcion = input("Ingresar Opcion")
    opc = int(input())

    if opc == 1:
        for times in range(0, 5):
            print(lista[times])
            
            
    if opc == 2:
        salir = False
