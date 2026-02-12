#!/usr/bin/python3

import random


PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'
LAGARTO = 'lagarto'
SPOCK = 'spock'


# Mapa de reglas: cada jugada mapea a las jugadas que derrota y el mensaje asociado.
# Para extender (ej. añadir 'lagarto' o 'spock') actualiza solamente este diccionario.
mapa_ganador = {
    PIEDRA: {TIJERAS: 'Piedra rompe tijeras.',LAGARTO:'Piedra aplasta lagarto'},
    PAPEL: {PIEDRA: 'Papel cubre piedra.',SPOCK: 'Papel desautoriza Spock'},
    TIJERAS: {PAPEL: 'Tijeras cortan papel.',LAGARTO: 'Tijeras decapita lagarto'},
    LAGARTO: {PAPEL: 'Lagarto come papel',SPOCK:'Lagarto envenena a Spock'},
    SPOCK: {TIJERAS: 'Spock rompe tijera', PIEDRA: 'Spock vaporiza piedra'}
}


def evaluar_juego(accion_usuario, accion_computadora):
    
    """Decide el resultado usando `mapa_ganador`.

    - Empate cuando las acciones son iguales.
    - Si `accion_computadora` está en `mapa_ganador[accion_usuario]` -> usuario gana.
    - Si `accion_usuario` está en `mapa_ganador[accion_computadora]` -> usuario pierde.
    - Si no existe la regla -> aviso de regla indefinida.
    """

    if accion_usuario == accion_computadora:
        print(f"Usuario y ordenador eligieron {accion_usuario}. ¡Empate!")
        return

    victorias_usuario = mapa_ganador.get(accion_usuario, {})
    if accion_computadora in victorias_usuario:
        print(f"{victorias_usuario[accion_computadora]} ¡Has ganado!")
        return

    victorias_computadora = mapa_ganador.get(accion_computadora, {})
    if accion_usuario in victorias_computadora:
        print(f"{victorias_computadora[accion_usuario]} ¡Has perdido!")
        return

    # Fallback para reglas no definidas (mantiene robustez al añadir jugadas)
    print(f"No hay regla definida para '{accion_usuario}' vs '{accion_computadora}'. Resultado indefinido.")


def main():
    # Derivar opciones a partir de `mapa_ganador` para que sólo esa estructura requiera cambios.
    opciones = list(mapa_ganador.keys())

    while True:
        accion_usuario = input(f"\nElige una opción: {', '.join(opciones)}: ")
        if accion_usuario not in opciones:
            print(f"Opción inválida. Opciones válidas: {', '.join(opciones)}")
            continue

        accion_computadora = random.choice(opciones)
        print(f"\nHas elegido {accion_usuario}. El ordenador eligió {accion_computadora}\n")
        evaluar_juego(accion_usuario, accion_computadora)


if __name__ == "__main__":
    main()
