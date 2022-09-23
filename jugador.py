from ficha import Ficha



class Jugador:

    def __init__(self):
        self.miFicha=Ficha()
        pass

    def realizar_jugada(self,unTablero):
        x=-1
        y=-1
        while unTablero.verificarJugada(x,y)==False:
            
            while x>2 or x<0:
                x=int(input("Ingresa la fila"))
            while x>2 or x<0:
                y=int(input("Ingresa la columna"))
        unTablero.matriz[x][y]= self.miFicha.simbolo
        return unTablero
