
from jugador import Jugador
from tablero import Tablero


class Juego:

    def __init__(self):

        self.miJugador=Jugador()
        self.miTablero=Tablero()
    def jugarTriqui(self):

        self.miJugador.miFicha.simbolo="x"
        self.miJugador.realizar_jugada(self.miTablero)
        self.miJugador.realizar_jugada(self.miTablero)
miJuego=Juego()
miJuego.jugarTriqui()


