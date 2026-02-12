#!/usr/bin/python3

import random
from typing import Dict, Mapping


PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'
LAGARTO = 'lagarto'
SPOCK = 'spock'


# Mapa de reglas por defecto (se puede sobreescribir al instanciar la clase).
mapa_ganador = {
    PIEDRA: {TIJERAS: 'Piedra rompe tijeras.', LAGARTO: 'Piedra aplasta lagarto'},
    PAPEL: {PIEDRA: 'Papel cubre piedra.', SPOCK: 'Papel desautoriza Spock'},
    TIJERAS: {PAPEL: 'Tijeras cortan papel.', LAGARTO: 'Tijeras decapitan lagarto'},
    LAGARTO: {PAPEL: 'Lagarto come papel', SPOCK: 'Lagarto envenena a Spock'},
    SPOCK: {TIJERAS: 'Spock rompe tijera', PIEDRA: 'Spock vaporiza piedra'},
}


class JuegoPiedraPapelTijeras:

    """
    Juego Rock-Paper-Scissors (configurable vía `mapa_ganador`) orientado a objetos.
    - Mantiene `self.mapa_ganador` y `self.opciones`.
    - Métodos principales usan `self` (instancia) para facilitar extensión y pruebas.
    """

    def __init__(self, reglas: Mapping[str, Mapping[str, str]] = None) -> None:
        self.mapa_ganador: Dict[str, Dict[str, str]] = (
            {**mapa_ganador} if reglas is None else dict(reglas)
        )
        self.opciones = list(self.mapa_ganador.keys())

    def evaluar_juego(self, accion_usuario: str, accion_computadora: str) -> None:

        """
        Evalúa y muestra el resultado entre `accion_usuario` y `accion_computadora`.
        La salida por consola se mantiene para compatibilidad con la versión procedural.
        """

        if accion_usuario == accion_computadora:
            print(f"Usuario y ordenador eligieron {accion_usuario}. ¡Empate!")
            return

        victorias_usuario = self.mapa_ganador.get(accion_usuario, {})
        if accion_computadora in victorias_usuario:
            print(f"{victorias_usuario[accion_computadora]} ¡Has ganado!")
            return

        victorias_computadora = self.mapa_ganador.get(accion_computadora, {})
        if accion_usuario in victorias_computadora:
            print(f"{victorias_computadora[accion_usuario]} ¡Has perdido!")
            return

        print(
            f"No hay regla definida para '{accion_usuario}' vs '{accion_computadora}'. Resultado indefinido."
        )

    def iniciar(self) -> None:

        """Bucle principal del juego que pide entrada al usuario y evalúa rondas."""

        while True:
            accion_usuario = input(f"\nElige una opción: {', '.join(self.opciones)}: ")
            if accion_usuario not in self.opciones:
                print(f"Opción inválida. Opciones válidas: {', '.join(self.opciones)}")
                continue

            accion_computadora = random.choice(self.opciones)
            print(f"\nHas elegido {accion_usuario}. El ordenador eligió {accion_computadora}\n")
            self.evaluar_juego(accion_usuario, accion_computadora)


def evaluar_juego_procedural(accion_usuario: str, accion_computadora: str) -> None:
    juego = JuegoPiedraPapelTijeras()
    juego.evaluar_juego(accion_usuario, accion_computadora)


def main() -> None:
    juego = JuegoPiedraPapelTijeras()
    juego.iniciar()


if __name__ == "__main__":
    main()

