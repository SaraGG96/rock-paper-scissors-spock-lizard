import pytest
from enum import Enum
from src.piedra_papel_tijeras import (
    PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK,
    mapa_ganador
)


class AccionJuego(Enum):
    """Mapeo de acciones del juego"""
    Piedra = PIEDRA
    Papel = PAPEL
    Tijeras = TIJERAS
    Lagarto = LAGARTO
    Spock = SPOCK


class ResultadoJuego(Enum):
    """Resultados posibles del juego"""
    Empate = 'empate'
    Victoria = 'victoria'
    Derrota = 'derrota'


def evaluar_juego(accion_usuario, accion_computadora):
    """Evalúa el resultado del juego entre dos acciones AccionJuego.
    
    Returns:
        ResultadoJuego: Empate, Victoria o Derrota
    """
    usuario_val = accion_usuario.value
    computadora_val = accion_computadora.value
    
    if usuario_val == computadora_val:
        return ResultadoJuego.Empate
    
    victorias_usuario = mapa_ganador.get(usuario_val, {})
    if computadora_val in victorias_usuario:
        return ResultadoJuego.Victoria
    
    victorias_computadora = mapa_ganador.get(computadora_val, {})
    if usuario_val in victorias_computadora:
        return ResultadoJuego.Derrota
    
    return ResultadoJuego.Empate


@pytest.mark.empate
def test_empate():
    '''
    Partidas con empate
    '''

    assert ResultadoJuego.Empate == evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Piedra)

    assert ResultadoJuego.Empate == evaluar_juego(
        accion_usuario=AccionJuego.Tijeras, 
        accion_computadora=AccionJuego.Tijeras)

    assert ResultadoJuego.Empate == evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Papel)

@pytest.mark.piedra
def test_piedra_pierde():
    '''
    Piedra pierde con Papel 
    '''
    assert ResultadoJuego.Victoria == evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Piedra)

@pytest.mark.piedra
def test_piedra_gana():
    '''
    Piedra gana a Tijeras
    '''
    assert ResultadoJuego.Derrota == evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Piedra)

@pytest.mark.papel
def test_papel_pierde():
    '''
    Papel pierde con Tijeras
    '''
    assert ResultadoJuego.Victoria == evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Papel)

@pytest.mark.papel
def test_papel_gana():
    '''
    Papel gana a Piedra
    '''
    assert ResultadoJuego.Derrota == evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Papel)

@pytest.mark.tijeras
def test_tijeras_pierde():
    '''
    Tijeras pierde con Piedra 
    '''
    assert ResultadoJuego.Victoria == evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Tijeras)

@pytest.mark.tijeras
def test_tijeras_gana():
    '''
    Tijeras gana a Papel 
    '''
    assert ResultadoJuego.Derrota == evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Tijeras)
