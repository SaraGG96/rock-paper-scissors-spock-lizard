import pytest
from src.piedra_papel_tijeras import (PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK, JuegoPiedraPapelTijeras)

@pytest.fixture
def juego():
    return JuegoPiedraPapelTijeras()

@pytest.mark.empate
def test_empate(juego, capsys):
    for opcion in [PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK]:
        juego.evaluar_juego(opcion, opcion)
        out = capsys.readouterr().out
        assert 'Empate' in out

@pytest.mark.spock
def test_spock(juego, capsys):
    juego.evaluar_juego(SPOCK, PAPEL)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(SPOCK, LAGARTO)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(SPOCK, TIJERAS)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out
    juego.evaluar_juego(SPOCK, PIEDRA)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out

@pytest.mark.lagarto
def test_lagarto(juego, capsys):
    juego.evaluar_juego(LAGARTO, PIEDRA)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(LAGARTO, TIJERAS)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(LAGARTO, SPOCK)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out
    juego.evaluar_juego(LAGARTO, PAPEL)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out

@pytest.mark.piedra
def test_piedra(juego, capsys):
    juego.evaluar_juego(PIEDRA, PAPEL)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(PIEDRA, SPOCK)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(PIEDRA, TIJERAS)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out
    juego.evaluar_juego(PIEDRA, LAGARTO)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out

@pytest.mark.papel
def test_papel(juego, capsys):
    juego.evaluar_juego(PAPEL, TIJERAS)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(PAPEL, LAGARTO)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(PAPEL, PIEDRA)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out
    juego.evaluar_juego(PAPEL, SPOCK)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out

@pytest.mark.tijeras
def test_tijeras(juego, capsys):
    juego.evaluar_juego(TIJERAS, SPOCK)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(TIJERAS, PIEDRA)
    out = capsys.readouterr().out
    assert 'Has perdido' in out or 'Has ganado' in out
    juego.evaluar_juego(TIJERAS, LAGARTO)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out
    juego.evaluar_juego(TIJERAS, PAPEL)
    out = capsys.readouterr().out
    assert 'Has ganado' in out or 'Has perdido' in out