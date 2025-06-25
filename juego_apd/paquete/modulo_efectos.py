import pygame

def efecto_fade_out(pantalla):
    """
    Esta función hace un efecto de fadeout en la pantalla
    """
    for alpha in range(0, 255, 10):
        overlay = pygame.Surface(pantalla.get_size())
        overlay.fill((0, 0, 0))
        overlay.set_alpha(alpha)
        pantalla.blit(overlay, (0, 0))
        pygame.display.update()
        pygame.time.delay(55)

def scroll_fondo(config, fondo):
    """
    Esta función hace un efecto parallax (o sea, que se mueva en horizontal infinitamente) sobre un fondo elegido
    """
    ANCHO_FONDO = fondo.get_width()
    vel_parallax = 0.5

    config['pos_x_scroll'] -= vel_parallax

    if config['pos_x_scroll'] <= -ANCHO_FONDO:
        config['pos_x_scroll'] = 0
    config['pantalla'].blit(fondo, (config['pos_x_scroll'], 0))
    config['pantalla'].blit(fondo, (config['pos_x_scroll'] + ANCHO_FONDO, 0))

