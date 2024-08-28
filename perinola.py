from random import choice

fichas = [5, 5, 5, 5]
nombres = ["j1", "j2", "j3", "j4"]
apuesta = 0
tiro = "Pon 1"

def tirarPerinola():
    caras = ("Pon 1", "Toma 2", "Todos Ponen",
     "Toma 1", "Pon 2", "Toma Todo")
    return choice(caras)