"""
En este módulo manejo la lógica interna del juego en general
"""

from paquete.modulo_solicitudes import preguntar_int_en_rango
from paquete.modulo_jugadores import *
from paquete.modulo_acertijos import *
from paquete.modulo_resultados import *
from paquete.listado_acertijos import lista_acertijos
lista_jugadores = []

def iniciar_juego():
    cantidad_jugadores = preguntar_int_en_rango("Ingrese cantidad de jugadores: ", 1, 10)
    for i in range(cantidad_jugadores):
        jugador = ingreso_jugador(i+1)
        comenzar_salas(jugador)
        lista_jugadores.append(jugador)
    mostrar_resultados(lista_jugadores)

def comenzar_salas(jugador):
    sala_actual = 1
    sigue_jugando = True

    while sala_actual <= 4 and sigue_jugando:
        gano_ronda = False
        intentos = 2
        print(f"Sala actual: {sala_actual} - Jugador {jugador['nombre']}")
        
        acertijo = generar_acertijo(lista_acertijos, jugador)
        respuesta = preguntar_acertijo(acertijo)
        respuesta_valida = validar_respuesta(respuesta, acertijo)

        while intentos != 0 and not respuesta_valida:
            print(f"Incorrecto, te queda {intentos} intento/s")
            intentos -= 1
            respuesta = preguntar_acertijo(acertijo)
            respuesta_valida = validar_respuesta(respuesta, acertijo)

        if intentos == 0:
            print(f'Jugador {jugador['nombre']} perdió!')
            sigue_jugando = False
        else:
            gano_ronda = True
            if sala_actual == 4:
                print(f"Jugador {jugador['nombre']} ha ganado las salas!")
            else:
                print(f"Jugador {jugador['nombre']} acertó, pasa a la siguiente sala!")
        jugador['ultima_sala'] = sala_actual
        añadir_puntuacion(jugador, sala_actual-1, gano_ronda)
        sala_actual += 1
