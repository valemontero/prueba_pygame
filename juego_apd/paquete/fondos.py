import pygame
from paquete.modulo_efectos import scroll_fondo

fondos = {
    'background':{
        'ruta': 'juego_apd/images/fondo.jpg',
        'imagen': None
    },
    'background_ingreso': {
        'ruta': 'juego_apd/images/ingreso_fondo.jpg',
        'imagen': None
    },
    'juego':{
        'ruta': 'juego_apd/images/sala.jpg',
        'imagen': None
    },
    'win': {
        'ruta': 'juego_apd/images/win.jpg',
        'imagen': None
    },
    'loss':{
        'ruta': 'juego_apd/images/loss.jpg',
        'imagen': None
    }
}

imagenes = {
    
}
def normalizar_fondos(ancho, alto):
    """
    Retorna un arreglo con los fondos ya normalizados al ancho y alto definido
    """
    for fondo, datos in fondos.items():
        imagen = pygame.image.load(datos['ruta'])
        imagen = pygame.transform.scale(imagen, (ancho, alto))
        fondos[fondo]['imagen'] = imagen
    return fondos

def gestionar_fondos_estados(config, fondos):
    if config['estado_actual'] == 'menu' or config['estado_actual'] == 'preparacion':
        config['pantalla'].blit(fondos['background']['imagen'], (0, 0))      
    elif config['estado_actual'] == 'preparacion_ingreso':
        scroll_fondo(config, fondos['background_ingreso']['imagen'])
    elif config['estado_actual'] == 'juego':
            config['pantalla'].blit(fondos['juego']['imagen'], (0, 0))
    elif config['estado_actual'] == 'game_win':
            config['pantalla'].blit(fondos['win']['imagen'], (0, 0))
    elif config['estado_actual'] == 'game_over':
            config['pantalla'].blit(fondos['loss']['imagen'], (0, 0))
    elif config['estado_actual'] == 'ganadores':
            config['pantalla'].fill((0, 0, 0))

    

