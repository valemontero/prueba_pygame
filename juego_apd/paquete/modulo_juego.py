import pygame, sys
# Módulos
from paquete.modulo_texto import *
from paquete.estados.modulo_opciones import *
from paquete.estados.modulo_eventos import *
from paquete.modulo_jugadores import *
from paquete.modulo_sonidos import *
from paquete.modulo_efectos import *
from paquete.modulo_acertijos import generar_acertijo

# Datos y estructuras
from paquete.colores import * 
from paquete.fondos import *
from paquete.acertijos import *

# Inicializaciones
pygame.init()
pygame.font.init()
pygame.mixer.init()
ANCHO, ALTO = 800, 600
clock = pygame.time.Clock()
pygame.display.set_caption("Preguntas y Respuestas")


# Normalización de fondos
fondos = normalizar_fondos(ANCHO, ALTO) 

# Listado de sonidos
VOLUMEN_SONIDOS = 0.20
sonidos = {
    'empezar_jugar': pygame.mixer.Sound('juego_apd/sounds/empezar_jugar.wav'),
    'aceptar': pygame.mixer.Sound('juego_apd/sounds/aceptar.wav'),
    'volver': pygame.mixer.Sound('juego_apd/sounds/volver.wav'),
    'salir': pygame.mixer.Sound('juego_apd/sounds/salir.wav'),
    'incorrecto': pygame.mixer.Sound('juego_apd/sounds/incorrecto.wav'),
    'acierto': pygame.mixer.Sound('juego_apd/sounds/acierto.wav'),
    'game_over': pygame.mixer.Sound('juego_apd/sounds/game_over.ogg'),
    'game_win': pygame.mixer.Sound('juego_apd/sounds/game_win.ogg')
}

config = {
    'pantalla': pygame.display.set_mode((ANCHO, ALTO)),
    'fuente': pygame.font.SysFont(None, 40),
    'fuente_chica': pygame.font.SysFont('opensans.ttf', 24),
    'estado_actual': 'menu',
    'sonidos': sonidos,
    'VOLUMEN_SONIDOS': VOLUMEN_SONIDOS,
    'mensaje_error': '',
    'pos_x_scroll': 0
}

def iniciar_juego():
# Usos en ejecución
    musica_fondo_actual = None
    seguir_ejecucion = True

    LIMITE_SEGUNDOS = 30
    EVENTO_TEMPORIZADOR = pygame.USEREVENT
    pygame.time.set_timer(EVENTO_TEMPORIZADOR, 1000)

    estado_juego = {
        'cant_jugadores': '',
        'nombre_jugador': '',
        'numero_jugador_actual': 1,
        'lista_jugadores': []
    } 

    salas = {
        'sala_actual': 1,
        'intentos': 2,
        'gano_ronda': False,
        'sigue_jugando': True,
        'consigna_generada': False,
        'respuesta_jugador': '',
        'tiempo_restante': LIMITE_SEGUNDOS
    }
    
    #Main de ejecución del juego
    while seguir_ejecucion:
        eventos = pygame.event.get()
        estado_actual = config['estado_actual']
        musica_fondo_actual = manejar_musica(estado_actual, musica_fondo_actual, VOLUMEN_SONIDOS, 1500)

        #Gestión de fondos de Estados
        gestionar_fondos_estados(config, fondos)
        # if estado_actual == 'menu' or estado_actual == 'preparacion':
        #     config['pantalla'].blit(fondos['background']['imagen'], (0, 0))      
        # elif estado_actual == 'preparacion_ingreso':
        #     pos_x_fondo_scroll = scroll_fondo(config['pantalla'], fondos['background_ingreso']['imagen'], pos_x_fondo_scroll)
        # elif estado_actual == 'juego':
        #     config['pantalla'].blit(fondos['juego']['imagen'], (0, 0))
        # elif estado_actual == 'game_win':
        #     config['pantalla'].blit(fondos['win']['imagen'], (0, 0))
        # elif estado_actual == 'game_over':
        #     config['pantalla'].blit(fondos['loss']['imagen'], (0, 0))
        # elif estado_actual == 'ganadores':
        #     config['pantalla'].fill(NEGRO)

        # Gestión de Estados
        if estado_actual == 'menu':
            op_menu = generar_opciones_menu(config, MORADO, MORADO_CLARO)
        elif estado_actual == 'preparacion':
            op_preparacion = generar_opciones_preparacion(config, MORADO, MORADO_CLARO)
            actualizar_pantalla_preparacion(config, estado_juego['cant_jugadores'], op_preparacion)
        elif estado_actual == 'preparacion_ingreso':
            opciones_ingreso = generar_opciones_ingreso(config, estado_juego)
            # actualizar_pantalla_ingreso(config, estado_juego['nombre_jugador'], opciones_ingreso)

        elif estado_actual == 'juego':
            jugador_actual = estado_juego['lista_jugadores'][estado_juego['juega_ahora']]
            if not salas['consigna_generada']:
                consigna = generar_acertijo(lista_acertijos, jugador_actual)
                salas['consigna_generada'] = True
                jugador_actual['ultima_sala'] = salas['sala_actual']
                tiempo_restante = LIMITE_SEGUNDOS
                print(jugador_actual)

            consignas_jugador = generar_pantalla_salas(config, salas['intentos'], consigna, tiempo_restante)
            actualizar_pantalla_salas(config, salas['respuesta_jugador'], consignas_jugador['respuesta'])

            if tiempo_restante == 0 or salas['intentos'] == 0:
                inicio_game_over = pygame.time.get_ticks()
                config['estado_actual'] = 'game_over'
                reiniciar_config_salas(salas, LIMITE_SEGUNDOS)
                reproducir_sonido(sonidos, 'game_over', VOLUMEN_SONIDOS)
            elif salas['gano_ronda']:
                if salas['sala_actual'] == 4:
                    inicio_game_win = pygame.time.get_ticks()
                    añadir_puntuacion(jugador_actual, (salas['sala_actual']-1), salas['gano_ronda'])
                    salas['sala_actual'] += 1
                    config['estado_actual'] = 'game_win'
                    reproducir_sonido(sonidos, 'game_win', VOLUMEN_SONIDOS)
                    reiniciar_config_salas(salas, LIMITE_SEGUNDOS)
                    salas['gano_ronda'] = False
                else:
                    añadir_puntuacion(jugador_actual, (salas['sala_actual']-1), salas['gano_ronda'])
                    salas['sala_actual'] += 1
                    salas['intentos'] = 2
                    salas['consigna_generada'] = False
                    salas['gano_ronda'] = False


        elif estado_actual == 'game_over':
            crear_texto(config['pantalla'], config['fuente'], '¡Perdiste!', MORADO, (350, 200), True)
            tiempo_transcurrido_game_over = pygame.time.get_ticks() - inicio_game_over
            if tiempo_transcurrido_game_over >= 5000:
                validar_terminado_juego(config, estado_juego)
                efecto_fade_out(config['pantalla'])
        
        elif estado_actual == 'game_win':
            imagen_win = pygame.image.load('juego_apd/images/win_label.png')
            config['pantalla'].blit(imagen_win, (350, 350))
            tiempo_transcurrido_game_win = pygame.time.get_ticks() - inicio_game_win
            if tiempo_transcurrido_game_win >= 5000:
                validar_terminado_juego(config, estado_juego)
                efecto_fade_out(config['pantalla'])


        #Gestión de eventos
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Eventos de clickeo
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if estado_actual == 'menu':
                        manejar_eventos_menu(config, event, op_menu)
                    elif estado_actual == 'preparacion':
                        manejar_eventos_preparacion(config, estado_juego, event, op_preparacion)
                    elif estado_actual == 'preparacion_ingreso':
                        manejar_eventos_ingreso(config, estado_juego, event, opciones_ingreso)
                    elif estado_actual == 'juego':
                        if consignas_jugador['boton_responder'].collidepoint(event.pos):
                            if consigna['respuesta'] == salas['respuesta_jugador']:
                                reproducir_sonido(sonidos, 'acierto', VOLUMEN_SONIDOS, 2000)
                                salas['gano_ronda'] = True
                                salas['respuesta_jugador'] = ''
                            else:
                                reproducir_sonido(sonidos, 'incorrecto', VOLUMEN_SONIDOS)
                                salas['intentos'] -= 1
            #Eventos de Tecleo 
            if event.type == pygame.KEYDOWN:
                if estado_actual == 'preparacion':
                    if event.key == pygame.K_BACKSPACE:
                        estado_juego['cant_jugadores'] = estado_juego['cant_jugadores'][:-1]
                    else:
                        if event.unicode.isdigit():
                            estado_juego['cant_jugadores'] += event.unicode  # Agrega el carácter escrito solo si es numérico
                elif estado_actual == 'preparacion_ingreso':
                    if event.key == pygame.K_BACKSPACE:
                        estado_juego['nombre_jugador'] = estado_juego['nombre_jugador'][:-1]
                    else:
                        estado_juego['nombre_jugador'] += event.unicode 
                elif estado_actual == 'juego':
                    if event.key == pygame.K_BACKSPACE:
                        salas['respuesta_jugador'] = salas['respuesta_jugador'][:-1]
                    else:
                        salas['respuesta_jugador'] += event.unicode
            
            if event.type == EVENTO_TEMPORIZADOR:
                if estado_actual == 'juego' and salas['consigna_generada']:
                    tiempo_restante -= 1
        

        clock.tick(60)
        pygame.display.flip()