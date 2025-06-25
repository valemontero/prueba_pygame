from paquete.modulo_sonidos import reproducir_sonido
from paquete.modulo_efectos import efecto_fade_out
from paquete.modulo_jugadores import crear_jugador
import pygame, sys


def manejar_eventos_menu(config, event, opciones):  
    estado_actual = config['estado_actual']
    sonidos = config['sonidos']
    VOLUMEN_SONIDOS = config['VOLUMEN_SONIDOS']

    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if estado_actual == 'menu':
                    if opciones[0].collidepoint(event.pos):
                        reproducir_sonido(sonidos, 'empezar_jugar', VOLUMEN_SONIDOS, 1500)
                        config['estado_actual'] = 'preparacion'
                    elif opciones[1].collidepoint(event.pos):
                        reproducir_sonido(sonidos, 'salir', VOLUMEN_SONIDOS, 600)
                        pygame.quit()
                        sys.exit()

def manejar_eventos_preparacion(config, estado_juego, event, opciones_preparacion):
    pantalla = config['pantalla']
    sonidos = config['sonidos']
    VOLUMEN_SONIDOS = config['VOLUMEN_SONIDOS']
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if opciones_preparacion['boton_iniciar'].collidepoint(event.pos):
                if estado_juego['cant_jugadores'] == '':
                    config['mensaje_error'] = 'Ingresa algo'
                    reproducir_sonido(sonidos, 'incorrecto', VOLUMEN_SONIDOS)
                elif int(estado_juego['cant_jugadores']) < 1 or int(estado_juego['cant_jugadores']) > 10:
                    config['mensaje_error'] = 'Números entre 0 y 10'
                    reproducir_sonido(sonidos, 'incorrecto', VOLUMEN_SONIDOS)
                else:
                    reproducir_sonido(sonidos, 'aceptar', 0.5, 1000)
                    efecto_fade_out(pantalla)
                    config['estado_actual'] = 'preparacion_ingreso'
            elif opciones_preparacion['boton_volver'].collidepoint(event.pos):
                    reproducir_sonido(sonidos, 'volver', 0.3, 500)
                    config['estado_actual'] = 'menu'

def manejar_eventos_ingreso(config, estado_juego, event, opciones_ingreso):
    sonidos = config['sonidos']
    VOLUMEN_SONIDOS = config['VOLUMEN_SONIDOS']
    if opciones_ingreso[1].collidepoint(event.pos):
        if estado_juego['nombre_jugador'].strip() == '':
            config['mensaje_error'] = 'Ingresa algo'
            reproducir_sonido(sonidos, 'incorrecto', VOLUMEN_SONIDOS)
        else:
            reproducir_sonido(sonidos, 'aceptar', 0.5, 1500)
            efecto_fade_out(config['pantalla'])
            crear_jugador(estado_juego['nombre_jugador'], estado_juego['lista_jugadores'])
            estado_juego['numero_jugador_actual'] += 1
            estado_juego['juega_ahora'] = len(estado_juego['lista_jugadores'])-1
            config['estado_actual'] = 'juego'
            estado_juego['nombre_jugador'] = ''
                    
