def crear_texto(pantalla, fuente, texto, color, pos=None, dibujar=False):
    texto_creado = fuente.render(texto, True, color)
    if dibujar and pos != None:
        pantalla.blit(texto_creado, pos)
    return texto_creado