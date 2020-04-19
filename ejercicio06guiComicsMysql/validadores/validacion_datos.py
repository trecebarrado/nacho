import re

expresion_texto = "^(?![_\-\.\s\>\|\]\)]).+[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ]{0,50}(?<![_\-\.\<\|\[\(])$"
expresion_paginas = "^[0-9]{1,4}$"
expresion_tapa = "(^Blanda$)|(^Dura$)"
expresion_coleccion = "(^si$)|(^no$)"

def validar_texto(txt):
    validador_texto = re.compile(expresion_texto)
    return validador_texto.match(txt)

def validar_paginas(num):
    validador_paginas = re.compile(expresion_paginas)
    return validador_paginas.match(num)

def validar_tapa(sel):
    validador_tapa = re.compile(expresion_tapa)
    return validador_tapa.match(sel)

def validar_coleccion(sel):
    validador_coleccion = re.compile(expresion_coleccion)
    return validador_coleccion.match(sel)
