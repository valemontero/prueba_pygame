"""
En este módulo manejo todas las funciones para mostrar distintos tipos de resultados
"""

from paquete.modulo_validaciones import *

def mostrar_jugadores_mayor_puntaje(lista_jugadores: list):
    mayor_puntaje = obtener_mayor_puntaje(lista_jugadores)
    print(f"Jugador/es con mayor puntaje en todo el juego: ")
    for jugador in lista_jugadores:
        if jugador['puntaje_total'] == mayor_puntaje:
            print(f"Jugador {jugador['nombre']} - Puntaje total: {jugador['puntaje_total']}")


def obtener_mayor_puntaje(lista_jugadores: list) -> int:
    mayor_puntaje = 0
    for jugador in lista_jugadores:
        if jugador['puntaje_total'] > mayor_puntaje:
            mayor_puntaje = jugador['puntaje_total']
    return mayor_puntaje


def mostrar_jugadores_mas_lejos(lista_jugadores: list):
    hay_ganadores = validar_ganadores(lista_jugadores)
    print(f"Jugador/es que llegó o llegaron más lejos: ")
    if hay_ganadores:
        print("Hay ganador/es!")
        for jugador in lista_jugadores:
            if jugador['estado_final'] == 'Completó':
                print(f"Jugador {jugador['nombre']} completó el juego")
    else:
        sala_mas_lejana_alcanzada = obtener_sala_mas_lejos(lista_jugadores)
        for jugador in lista_jugadores:
            if jugador['ultima_sala'] == sala_mas_lejana_alcanzada:
                print(f"Jugador {jugador['nombre']} llegó hasta la sala {sala_mas_lejana_alcanzada}")

def obtener_sala_mas_lejos(lista_jugadores: list) -> int:
    sala_mas_lejana = 1
    for jugador in lista_jugadores:
        if jugador['ultima_sala'] > sala_mas_lejana:
            sala_mas_lejana = jugador['ultima_sala']
    return sala_mas_lejana

def mostrar_lista_jugadores_sala_uno(lista_jugadores: list) -> int:
    print("Jugador/es que quedaron en la primer sala: ")
    hubo_jugadores_no_pasaron = validar_jugadores_no_pasaron_sala_uno(lista_jugadores)
    if hubo_jugadores_no_pasaron:
        for jugador in lista_jugadores:
            if jugador['ultima_sala'] == 1:
                print(f"Jugador {jugador['nombre']} no pudo pasar la primer sala")
    else:
        print("Todos los jugadores pudieron pasar la primer sala")

def mostrar_jugadores(lista_jugadores: list):
    for numero, jugador in enumerate(lista_jugadores):
        print(f"Jugador {numero+1}")
        print(f"Nombre: {jugador['nombre']}")
        print(f"Puntaje por sala:")
        for sala, puntaje in enumerate(jugador['puntaje_sala']):
            print(f"Sala {sala+1}: {puntaje}")
        print(f"Puntaje total: {jugador['puntaje_total']}")


def mostrar_resultados(lista_jugadores: list):
    mostrar_jugadores(lista_jugadores)
    input("Para proceder a mostrar los resultados del torneo, presiona ENTER.")
    mostrar_jugadores_mayor_puntaje(lista_jugadores)
    mostrar_jugadores_mas_lejos(lista_jugadores)
    mostrar_lista_jugadores_sala_uno(lista_jugadores)
