from random import choices
class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def darFicha(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def sacarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No hay suficientes fichas para sacar")
        self.fichas -= cuantas
    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas
    def sinFichas(self):
        return self.fichas == 0