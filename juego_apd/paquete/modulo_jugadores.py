def crear_jugador(nombre, lista_jugadores):
    jugador = {
            "nombre": nombre,
            'puntaje_sala': [],
            'puntaje_total': 0,
            'estado_final': 'No completó',
            'ultima_sala': 1,
            'acertijos_preguntados': []
            }
    lista_jugadores.append(jugador)

def añadir_puntuacion(jugador, sala_actual, gano_ronda):
    if gano_ronda:
        salas = [10, 25, 30, 35]
        jugador['puntaje_sala'].append(salas[sala_actual])
        print(sala_actual)
        jugador['puntaje_total'] += salas[sala_actual]
        if jugador['ultima_sala'] == 4:
            jugador['estado_final'] = 'Completó'

def reiniciar_config_salas(salas, LIMITE_SEGUNDOS):
    salas['tiempo_restante'] = LIMITE_SEGUNDOS
    salas['intentos'] = 2
    salas['sala_actual'] = 1
    salas['consigna_generada'] = False
    salas['sigue_jugando'] = False
    salas['respuesta_jugador'] = ''

def validar_terminado_juego(config, estado_juego):
    if estado_juego['numero_jugador_actual'] > int(estado_juego['cant_jugadores']):
        config['estado_actual'] = 'ganadores'
    else:
        config['estado_actual'] = 'preparacion_ingreso'
