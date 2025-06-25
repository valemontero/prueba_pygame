import pygame
from paquete.modulo_texto import crear_texto
from paquete.colores import *

def dibujar_boton(pantalla, fuente, texto, pos, tamaño, color_rect, color_text):
    """
    Dibuja un botón con texto centrado
    """
    rect = pygame.Rect(pos[0], pos[1], tamaño[0], tamaño[1])
    pygame.draw.rect(pantalla, color_rect, rect)

    superficie_texto = crear_texto(pantalla, fuente, texto, color_text)
    texto_pos = superficie_texto.get_rect(center=rect.center)
    pantalla.blit(superficie_texto, texto_pos)


    return rect

def generar_opciones_menu(config, color_rect, color_text):
    """
    Dibuja las opciones del menú en la pantalla:
    opciones[0]: Jugar
    opciones[1]: Salir
    """
    pos_rect_1 = (150, 350)
    pos_rect_2 = (450, 350)
    tamaño = (200, 100)
    pantalla, fuente = config['pantalla'], config['fuente']


    opciones = [
            dibujar_boton(pantalla, fuente, 'Jugar', pos_rect_1, tamaño, color_rect, color_text), # Botón jugar
            dibujar_boton(pantalla, fuente, 'Salir', pos_rect_2, tamaño, color_rect, color_text), # Botón salir
            ]

    return opciones

def actualizar_recuadro(pantalla, fuente, texto_ingresado, recuadro):
    texto = crear_texto(pantalla, fuente, texto_ingresado, BLANCO)
    texto_pos = texto.get_rect(center=recuadro.center)
    pantalla.blit(texto, texto_pos)
        
def generar_opciones_preparacion(config, color_rect, color_text):
    pos_rect_2 = (180, 375)
    pos_rect_3 = (425, 375)

    pantalla = config['pantalla']
    fuente = config['fuente']

    crear_texto(pantalla, fuente, 'Ingrese cantidad de jugadores', BLANCO, (190, 79), True)
    recuadro = pygame.Rect(180, 140, 440, 160)
    recuadro = pygame.draw.rect(pantalla, color_rect, recuadro)
    boton_iniciar = dibujar_boton(pantalla, fuente, 'Iniciar', pos_rect_2, (200, 100), color_rect, color_text)
    boton_volver = dibujar_boton(pantalla, fuente, 'Volver', pos_rect_3, (200, 100), color_rect, color_text)
    opciones = {
        'recuadro': recuadro,
        'boton_iniciar': boton_iniciar,
        'boton_volver': boton_volver
    }

    return opciones
    
def actualizar_pantalla_preparacion(config, cant_jugadores, opciones):
    recuadro_x = opciones['recuadro'].x
    recuadro_y = opciones['recuadro'].y
    pantalla = config['pantalla']
    fuente = config['fuente']

    actualizar_recuadro(pantalla, fuente, cant_jugadores, opciones['recuadro'])
    crear_texto(pantalla, fuente, config['mensaje_error'], ROJO, (recuadro_x, recuadro_y-30), True)



def generar_opciones_ingreso(config, estado_juego):
    if estado_juego['numero_jugador_actual'] > int(estado_juego['cant_jugadores']):
        config['estado_actual'] = 'ganadores'
    else: 
        pantalla = config['pantalla']
        fuente = config['fuente']
        nombre_jugador = estado_juego['nombre_jugador']
        config['mensaje_error']= ''
        
        recuadro = pygame.Rect(180, 140, 440, 160)
        texto_aviso = f"Ingrese nombre de jugador {estado_juego['numero_jugador_actual']}"
        aviso = crear_texto(pantalla, fuente, texto_aviso, BLANCO)
        opciones = [recuadro,
                    dibujar_boton(pantalla, fuente, 'Aceptar', (180, 400), (200, 100), MORADO, MORADO_CLARO)]
        pygame.draw.rect(pantalla, MORADO, recuadro)
        pantalla.blit(aviso, (190, 70))
        actualizar_pantalla_ingreso(config, nombre_jugador, opciones)
        return opciones

def actualizar_pantalla_ingreso(config, nombre_jugador, opciones):
    pantalla = config['pantalla']
    fuente = config['fuente']

    recuadro_x = opciones[0].x
    recuadro_y = opciones[0].y
    actualizar_recuadro(pantalla, fuente, nombre_jugador, opciones[0])
    crear_texto(pantalla, fuente, config['mensaje_error'], ROJO, (recuadro_x, recuadro_y-30), True)
    # mensaje = crear_texto(fuente, mensaje_error, ROJO)
    # pantalla.blit(mensaje,(recuadro_x, recuadro_y-30))

def generar_pantalla_salas(config, intentos, acertijo, tiempo):
    pantalla = config['pantalla']
    fuente = config['fuente_chica']

    crear_texto(pantalla, fuente, f'Tienes {intentos} intentos para responder', BLANCO, (290, 90), True)
    crear_texto(pantalla, fuente, f'Tiempo restante - {tiempo}', BLANCO, (330, 120), True)
    opciones = {
        'recuadro_consigna': dibujar_boton(pantalla, fuente, acertijo['consigna'], (120, 150), (560, 60), MORADO, MORADO_CLARO),
        'respuesta': dibujar_boton(pantalla, fuente, '', (300, 250), (200, 60), MORADO, NEGRO),
        'boton_responder': dibujar_boton(pantalla, fuente, 'Responder', (300, 400), (200, 60), MORADO, NEGRO)
    }
    return opciones


def actualizar_pantalla_salas(config, respuesta_jugador, recuadro):
    pantalla = config['pantalla']
    fuente = config['fuente_chica']

    actualizar_recuadro(pantalla, fuente, respuesta_jugador, recuadro)
