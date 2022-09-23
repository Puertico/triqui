from ficha import Ficha



class Jugador:

    def __init__(self):
        self.miFicha=Ficha()
        pass

    def realizar_jugada(self,unTablero):

        while x>2 and x<0:
            x=int(input("Ingresa la fila"))
        y=-1
        while x>2 and x<0:
            y=int(input("Ingresa la columna"))

        unTablero[x][y]= self.miFicha.simbolo

        return unTablero
