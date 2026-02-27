# Piedra, Papel, Tijeras, Lagarto, Spock

Proyecto realizado por:  
Sara García Garrido — [SaraGG96](https://github.com/SaraGG96)    
Lucas Iñarrea Barba —  [EdMorCa67](https://github.com/EdMorCa67) 

Este proyecto implementa el juego "Piedra, Papel, Tijeras, Lagarto, Spock" siguiendo buenas prácticas de diseño y extensibilidad. El código está preparado para ser fácilmente ampliado y probado, y se apoya en un diccionario de reglas para la lógica del juego.

## Estructura del proyecto

- `src/piedra_papel_tijeras.py`: Implementación principal del juego, reglas y lógica.
- `test/test_piedra_papel_tijera.py`: Casos de prueba automatizados con pytest.
- `pytest.ini`: Markers para tests parametrizados.
- `requirements-dev.txt`: Dependencias de desarrollo (incluye pytest).

## Reglas del juego

Las reglas siguen la variante popularizada por la serie "The Big Bang Theory":

- **Piedra** aplasta a Tijeras y Lagarto
- **Papel** cubre a Piedra y desautoriza a Spock
- **Tijeras** cortan Papel y decapitan Lagarto
- **Lagarto** come Papel y envenena a Spock
- **Spock** rompe Tijeras y vaporiza Piedra

El resultado puede ser victoria, derrota o empate según las elecciones de usuario y ordenador.

## Uso

Puedes ejecutar el juego en modo interactivo:

```bash
python -m src.piedra_papel_tijeras
```

O bien importar y reutilizar la clase `JuegoPiedraPapelTijeras` en tus propios scripts.

## Ejemplo de uso en código

```python
from src.piedra_papel_tijeras import JuegoPiedraPapelTijeras, PIEDRA, PAPEL

juego = JuegoPiedraPapelTijeras()
juego.evaluar_juego(PIEDRA, PAPEL)  # Muestra el resultado por consola
```

## Testing

El proyecto incluye tests automatizados con pytest. Para ejecutarlos:

```bash
pip install -r requirements-dev.txt
python -m pytest -v
```

Puedes filtrar por tipo de jugada usando markers, por ejemplo:

```bash
python -m pytest -v -m piedra
python -m pytest -v -m spock
```

## Extensión y personalización

- Puedes modificar el diccionario `mapa_ganador` para añadir nuevas reglas o variantes.
- La lógica está encapsulada en una clase para facilitar pruebas y ampliaciones.

