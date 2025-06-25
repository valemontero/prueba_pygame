"""
En este módulo reviso validaciones comunes
"""

def validar_texto_vacio(texto: str) -> bool:
    es_valido = True
    if texto.strip() == "":
        es_valido = False
    return es_valido

def preguntar_texto(mensaje: str) -> str:
    """
    Función para ingresar textos, valida que no sean vacío y retorna el texto ingresado
    """
    texto = input(mensaje).strip()
    while not validar_texto_vacio(texto):
        print("Debe ingresar texto, no dejar vacío")
        texto = input(mensaje).strip()
    return texto

def preguntar_entero(mensaje: str) -> int:
    numero = int(input(mensaje))
    return numero

def preguntar_int_en_rango(mensaje: str, min: int, max=None, mensaje_error=None) -> int:
    """
    Pregunta un número entero en en rango determinado de números, puede tener límite máximo o no
    Puede asignarse un mensaje de error personalizado en caso de que se quiera
    """
    numero = preguntar_entero(mensaje)
    if max is None:
        while numero < min:
            if mensaje_error != None:
                print(mensaje_error)
                numero = preguntar_entero(mensaje)
            else:
                print(f"Ingrese número mayor o igual a {min}")
                numero = preguntar_entero(mensaje)
    else:
        while numero < min or numero > max:
            if mensaje_error != None:
                print(mensaje_error)
                numero = preguntar_entero(mensaje)
            else:
                print(f"Ingrese valor dentro del rango {min} y {max}")
                numero = preguntar_entero(mensaje)
    return numero
