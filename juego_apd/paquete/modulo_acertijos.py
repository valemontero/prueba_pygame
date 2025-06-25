import random
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
