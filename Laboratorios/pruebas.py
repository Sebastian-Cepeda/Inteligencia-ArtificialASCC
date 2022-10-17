import random
#import time

laberinto = [['#', '#', '#', '#', '#', '#', '#', '#'],
             ['#', '+', ' ', ' ', ' ', '#', '#', '#'],
             ['#', ' ', '#', '*', ' ', '#', ' ', '#'],
             ['#', ' ', '#', ' ', ' ', ' ', '*', '#'],
             ['#', ' ', '#', ' ', '#', '#', ' ', '#'],
             ['#', ' ', ' ', ' ', '#', '#', ' ', '#'],
             ['#', '#', '#', '#', '#', '#', '#', '#']]

entinty_agente = '+'
entinty_agente_x = 1
entinty_agente_y = 1
destino_x = entinty_agente_x
destino_y = entinty_agente_y
entinty_objeto = '*'

def mover_entinty(agente, agente_x, agente_y, destino_x, destino_y):
    for i in range(0,5):
               #movimiento arriba entinty
        if laberinto[destino_y - 1][destino_x ] == ' ':
            laberinto[destino_y - 1][destino_x] = agente
            laberinto[agente_y][agente_x] = ' '

            aux_y = destino_y - 1
            agente_y = aux_y

            #movimiento abajo entinty_agente
            if laberinto[destino_y + 1][destino_x] == ' ':
                laberinto[destino_y + 1][destino_x] = agente
                laberinto[agente_y][destino_x] = ' '

                aux_y = destino_y + 1
                agente_y = aux_y
                
                print(agente_y)
                print(agente_x)

            
                #movimiento derecha entinty
                if laberinto[destino_y][destino_x + 1] == ' ':
                    laberinto[destino_y][destino_x + 1] = agente
                    laberinto[destino_y][destino_x] = ' '

                    aux_x = destino_x + 1
                    agente_x = aux_x
                
                    #movimiento izquierda entinty
                    if laberinto[destino_y][destino_x - 1] == ' ':
                        laberinto[destino_y][destino_x - 1] = agente
                        laberinto[destino_y][destino_x] = ' '

                        aux_x = destino_x - 1
                        agente_x = aux_x

        #MUESTRA DEL MOVIMIENTO
        for i in range(0,7):
            print(laberinto[i])
        
        print("Siquiente Movimiento")
        print(destino_x)
        print(destino_y)
        print(agente_x)
        print(agente_y)
        

def end_game():
    if laberinto[destino_x][destino_y] == '*':
        return "Fin del juego"



#Main

for i in range(0,7):
    print(laberinto[i])
    

print("Presentacion del movimeinto")


mover_entinty(entinty_agente, entinty_agente_x, entinty_agente_y, destino_x, destino_y)
    


print(laberinto[entinty_agente_y-1][entinty_agente_x])




