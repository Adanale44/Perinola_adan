import pytest

from Rondas import Ronda , Jugador

def test_agregar_jugador():

   ronda = Ronda()

   jugador = Jugador("Andres", 5)

   ronda.agregarJugador(jugador)

   assert len(ronda.jugadores) == 1

   assert ronda.jugadores[0].nombre == "Andres"



def test_agregar_jugador_sin_fichas():
   ronda = Ronda()

   jugador_sin_fichas = Jugador("Emi", 0)

   with pytest.raises(ValueError):

       ronda.agregarJugador(jugador_sin_fichas)



def test_sacar_jugadores_sin_fichas():

   ronda = Ronda()

   jugador1 = Jugador("Andres", 5)

   jugador2 = Jugador("Emi", 0)

   ronda.agregarJugador(jugador1)

   ronda.agregarJugador(jugador2)



   ronda.sacarJugadoresSinFichas()

   assert len(ronda.jugadores) == 1

   assert ronda.jugadores[0].nombre == "Andres"



def test_jugador_en_turno():

   ronda = Ronda()

   jugador1 = Jugador("Andres", 5)

   jugador2 = Jugador("Emi", 3)

  

   ronda.agregarJugador(jugador1)

   ronda.agregarJugador(jugador2)



   assert ronda.jugadorEnTurno() == jugador1



def test_pasar_turno():

   ronda = Ronda()

   jugador1 = Jugador("Andres", 5)

   jugador2 = Jugador("Emi", 3)



   ronda.agregarJugador(jugador1)

   ronda.agregarJugador(jugador2)



   ronda.pasarTurno()

   assert ronda.jugadores[0] == jugador2

   assert ronda.jugadores[1] == jugador1



def test_queda_un_solo_jugador():

   ronda = Ronda()

   jugador1 = Jugador("Andres", 5)

   ronda.agregarJugador(jugador1)

   assert ronda.quedaUnSoloJugador()

   jugador2 = Jugador("Emi", 3)