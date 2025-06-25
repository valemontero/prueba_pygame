"""
En este módulo manejo la generación acertijos, así como la pregunta y la validación de la respuesta
"""

import random
from paquete.modulo_solicitudes import *

def generar_acertijo(lista_acertijos: list, jugador: dict) -> dict:
    """
    Verifica que el acertijo que sea generado no se repita verificando el historial del jugador
    """
    acertijos_disponibles = []
    for i in range(len(lista_acertijos)):
        if i not in jugador['acertijos_preguntados']:
            acertijos_disponibles.append(i)

    acertijo_indice = random.choice(acertijos_disponibles)
    jugador['acertijos_preguntados'].append(acertijo_indice)
    acertijo = lista_acertijos[acertijo_indice]

    return acertijo

def preguntar_acertijo(acertijo: dict) -> str:
    """
    Retorna la respuesta del acertijo seleccionado
    """
    print(f"Consigna: {acertijo['consigna']}")
    respuesta = preguntar_texto("Ingrese su respuesta: ")
    return respuesta

def validar_respuesta(respuesta: str, acertijo: dict) -> bool:
    """
    Valida que la respuesta del acertijo sea correcta y retorna la validación
    """
    es_valida = False
    if respuesta == acertijo['respuesta']:
        es_valida = True
    return es_valida
