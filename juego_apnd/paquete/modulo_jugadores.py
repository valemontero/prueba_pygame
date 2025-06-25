"""
En este módulo manejo el ingreso de los datos de cada jugador y sus puntuaciones
"""

from paquete.modulo_solicitudes import preguntar_texto

def ingreso_jugador(numero_jugador):
    """
    Función que gestiona la lógica de ingreso de jugadores.
    """
    nombre = preguntar_texto(f"Ingrese nombre de jugador {numero_jugador}: ")
    jugador = {
        "nombre": nombre,
        'puntaje_sala': [],
        'puntaje_total': 0,
        'estado_final': 'No completó',
        'ultima_sala': 1,
        'acertijos_preguntados': []
        }
    return jugador

def añadir_puntuacion(jugador: dict, sala: int, gano_ronda: bool):
    salas = [10, 25, 30, 35]
    if gano_ronda:
        jugador['puntaje_sala'].append(salas[sala])
        jugador['puntaje_total'] += salas[sala]
        if jugador['ultima_sala'] == 4:
            jugador['estado_final'] = 'Completó'