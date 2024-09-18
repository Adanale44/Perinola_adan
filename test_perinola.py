from perinolaPrueba import Perinola 

def test_prueba():
    assert(True)

def test_constructor():
    p = Perinola()
    assert(p.cara_visible == 'Pon 1')

def test_repr():
    p = Perinola()
    msj = p.__repr__()
    assert("Salio:" in msj)
    assert(p.cara_visible in msj)

def test_tirar():
    p = Perinola()
    caras_posibles = ("Pon 1", "Toma 2", "Todos Ponen", "Toma 1", "Pon 2", "Toma Todo")
    for _ in range(1000):
        resultado = p.tirar()
        assert resultado in caras_posibles
