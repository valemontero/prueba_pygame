"""
En este módulo reviso validaciones específicas del juego
"""

def validar_jugadores_no_pasaron_sala_uno(lista_jugadores):
    hubo_jugadores_no_pasaron = False
    for jugador in lista_jugadores:
        if jugador['ultima_sala'] == 1:
            hubo_jugadores_no_pasaron = True
    return hubo_jugadores_no_pasaron

def validar_ganadores(lista_jugadores: list):
    """
    Verifica si existe algún ganador de entre los jugadores
    """
    hay_ganadores = False
    i = 0
    while i < len(lista_jugadores) and not hay_ganadores:
        if lista_jugadores[i]['estado_final'] == 'Completó':
            hay_ganadores = True
        i += 1
    return hay_ganadores