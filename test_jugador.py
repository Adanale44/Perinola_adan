from Jugador import Jugador

def test_constructor():
    j = Jugador("Jugador1", 6)

    assert(j.nombre == "Jugador1")
    assert(j.fichas == 6)

def test_constructur_sin_fichas():
    j = Jugador("Jugador1")
    assert(j.nombre == "Jugador1")
    assert(j.fichas == 5)


def test_dar_ficha():
    j = Jugador("Jugador1", 10)
    j.darFichas()
    assert(j.fichas == 11)