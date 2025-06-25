import pygame

def manejar_musica(estado, musica_actual, volumen, fade=0):
    """
    Esta función pone música dependiendo del estado actual del jugadorrr.
    """
    estado_actualizado = None
    if estado == 'menu' and musica_actual != 'menu':
        pygame.mixer.music.fadeout(fade)

        pygame.mixer.music.load('juego_apd/sounds/ocarina_background_theme.ogg')
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1, fade_ms=fade)
        estado_actualizado = estado
        
    elif estado == 'preparacion_ingreso' and musica_actual != 'preparacion_ingreso':
        pygame.mixer.music.fadeout(fade)

        pygame.mixer.music.load('juego_apd/sounds/ingreso.ogg')
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1, fade_ms=fade)
        estado_actualizado = estado
    elif estado == 'juego' and musica_actual != 'juego':
        pygame.mixer.music.fadeout(fade)

        pygame.mixer.music.load('juego_apd/sounds/musica_sala.ogg')
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1, fade_ms=fade)
        estado_actualizado = estado
    elif estado == 'game_over' or estado == 'game_win':
        pygame.mixer.music.stop()
    
    else:
        estado_actualizado = musica_actual
    return estado_actualizado
    
def reproducir_sonido(sonidos, nombre, volumen, espera=0):
    """
    Esta función reproduce un sonido específico
    """
    sonido = sonidos[nombre]
    sonido.set_volume(volumen)
    sonido.play()
    if espera != 0:
        pygame.time.wait(espera)