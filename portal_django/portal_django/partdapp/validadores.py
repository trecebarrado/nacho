import re

texto = "^(?![_\-\.\s\>\|\]\)]).+[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,50}(?<![_\-\.\<\|\[\(])$"
precio = "^\d{0,3}((\.|,)\d{0,2})?$"
telefono = "[6-9]{1}[0-9]{8}"
email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def validar_texto(txt):
    validador_texto = re.compile(texto)
    return validador_texto.match(txt)

def validar_precio(prc):
    validador_precio = re.compile(precio)
    return validador_precio.match(prc)

def validar_telefono(tfn):
    validador_telefono = re.compile(telefono)
    return validador_telefono.match(tfn)

def validar_email(mail):
    validador_email = re.compile(email)
    return validador_email.match(mail)
