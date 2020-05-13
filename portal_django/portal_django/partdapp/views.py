from django.shortcuts import render
from django.http.response import HttpResponse
from . import models
import random
import string
import os
from django.core.mail import send_mail
from django.http import JsonResponse
from . import validadores
from flask import redirect, url_for
# import logging

def inicio(request):
#     para ver sqls:
#     l = logging.getLogger('django.db.backends')
#     l.setLevel(logging.DEBUG)
#     l.addHandler(logging.StreamHandler())
    return render(request, "index.html")

def listado(request):
    res = models.Anuncio.objects.filter(emailvalido="SI").order_by("-id").prefetch_related('categoria')
    descripcion_buscador = ""
    total_resultados = res.count()
    descripcion_buscador = ""
    if "descripcion" in request.GET:
        descripcion_buscador = request.GET["descripcion"]
        res = res.filter(descripcion__contains = descripcion_buscador)
        total_resultados = res.count()
    materia_buscador = "-1"
    if "materia" in request.GET and request.GET["materia"] != "ninguna":
        materia_buscador = request.GET["materia"]
    if  materia_buscador != "-1":
        res = res.filter(categoria = materia_buscador)
        total_resultados = res.count()
    horario_buscador = ""
    if "horario" in request.GET and request.GET["horario"] != "ninguno":
        horario_buscador = request.GET["horario"]
    if  horario_buscador != "":
        res = res.filter(horario = horario_buscador)
        total_resultados = res.count()
    resultados_por_pagina = 5
    comienzo = 0
    if "comienzo" in request.GET:
        comienzo = int(request.GET["comienzo"])
    res = res[comienzo:comienzo + resultados_por_pagina]
    #total_resultados = models.Anuncio.objects.count()
    siguiente = comienzo + resultados_por_pagina
    anterior = comienzo - resultados_por_pagina
    hasta = 0
    if total_resultados < siguiente:
        hasta = total_resultados
    else:
        hasta = siguiente
    if total_resultados > 0:
        desde = siguiente - resultados_por_pagina + 1
    else:
        desde = 0
    context = {
        "anuncios" : res,
        "categorias" : models.Categoria.objects.order_by("id"),
        "descripcion_buscador" : descripcion_buscador,
        "materia_buscador" : int(materia_buscador),
        "horario_buscador" : horario_buscador,
        "siguiente" : siguiente,
        "anterior" : anterior,
        "desde" : desde,
        "hasta" : hasta,
        "total_resultados" : total_resultados
        }
    return render(request, "listado.html", context)

def contactar(request):
    id = request.GET["id"]
    anuncio = models.Anuncio.objects.get(pk = id)
    context = {
        "anuncio" : anuncio,
        "materias" : models.Categoria.objects.order_by("id")
        }
    return render(request, "contactar.html", context)

def form_contactar(request):
    mail_anunciante = request.GET["mail_anunciante"]
    nom_anunciante = request.GET["nom_anunciante"]
    nombre = request.GET["nombre"]
    descripcion = request.GET["descripcion"]
    email = request.GET["email"]
    telefono = request.GET["telefono"]
    nombre_list = nom_anunciante.split()
    nombre_mail = nombre_list[0]
    error = ""
    mensaje = "<p>Estimado "+nombre_mail+",<br><br>Hemos recibido la siguiente petición de contacto:<br><br>- Datos interesado:<br>Nombre: {}<br>E-mail: {}<br>Teléfono: {}<br><br>- Mensaje:<br>{}<br><br><br>Un saludo del equipo de <a style='color:green;' href='http://particulariadj.pythonanywhere.com';>Particularia<a/></p><br><p><img src='http://particulariadj.pythonanywhere.com/static/images/mail.jpg'/></p>".format(nombre, email, str(telefono), descripcion)
    try:
        send_mail(
            'PARTICULARIA. Petición de contacto.',
            '',
            'web.particularia@gmail.com',
            [mail_anunciante],
            fail_silently = False,
            html_message = mensaje)
    except Exception as e:
        error = str(e)
    return render(request, "contactarok.html")

def registro(request):
    return render(request, "registro.html")

def contacto(request):
    return render(request, "contacto.html")

def alta_login(request):
    return render(request, "alta-login.html")

def login(request):
    email_insertado = request.POST["email"]
    clave_insertada = request.POST["clave"]
    res = models.Usuarios.objects.filter(email = email_insertado, clave = clave_insertada)
    if len(res) == 0:
        context = {
                "error_login" : "E-mail o Contraseña incorrecta."
            }
        return render(request, "alta-login.html", context)
    else:
        usuario = res[0]
        request.session["id_usuario"] = usuario.id
        nom = usuario.nombre
        nombre = nom.split()
        context = {
                "nom_user" : nombre[0]
            }
        return render(request,"loginok.html", context)

def listado_usuario(request):
    usuario_actual = models.Usuarios.objects.get(pk = request.session["id_usuario"])
    res = models.Anuncio.objects.filter(usuario = usuario_actual).order_by("-id")
    context = {
                "anuncios" : res
            }
    return render(request,"listado-usuario.html", context)

def editar_anuncio(request):
    id = request.GET["id"]
    anuncio_a_editar = models.Anuncio.objects.get(pk = id)
    nombre_comp = anuncio_a_editar.nombre
    list_nombre = nombre_comp.split()
    nombre = list_nombre[0]
    if len(list_nombre) == 2:
        apellido = list_nombre[1]
    else:
        apellido = list_nombre[1] + " " + list_nombre[2]
    context = {
        "anuncio" : anuncio_a_editar,
        "materias" : models.Categoria.objects.order_by("id"),
        "nom" : nombre,
        "apell" : apellido
        }
    return render(request, "editar-anuncio.html", context)

def guardar_cambios_anuncio(request):
    anuncio = models.Anuncio.objects.get(pk = request.POST["id_anuncio"])
    nom_edit = request.POST["nom"]
    apell_edit = request.POST["apell"]
    nombre_ind = nom_edit + " " + apell_edit
    if not validadores.validar_texto(nombre_ind):
        return "El nombre introducido es incorrecto"
    anuncio.nombre = nombre_ind
    anuncio.descripcion = request.POST["descripcion"]
    imagen = str(anuncio.foto)
    check_borrar = request.POST.get("borrar", False)
    if check_borrar == "on":
        try:
            os.remove("/home/particulariadj/portal_django/partdapp/static/media/"+imagen)
        except:
            pass
        anuncio.foto = "images/profile/noperfil.png"
    check_am = request.POST.get("am", False)
    check_pm = request.POST.get("pm", False)
    if check_am == "on" and check_pm == "on":
        anuncio.horario = "Mañana y tarde"
    elif check_am == "on":
        anuncio.horario = "Mañanas"
    elif check_pm == "on":
        anuncio.horario = "Tardes"
    else:
        anuncio.horario = "Mañana y tarde"
    precio_ind = request.POST["precio"].replace(",",".")
    if not validadores.validar_precio(precio_ind):
        return "El precio por hora introducido es incorrecto"
    anuncio.precio = precio_ind
    telefono_ind = request.POST["telefono"]
    if not validadores.validar_telefono(telefono_ind):
        return "El telefono introducido es incorrecto"
    anuncio.telefono = telefono_ind
    email_ind = request.POST["email"]
    if not validadores.validar_email(email_ind):
        return "El e-mail introducido es incorrecto"
    anuncio.email = email_ind
    anuncio.tfno = "NO"
    check_tp = request.POST.get("ctp", False)
    if check_tp == "tp_on":
        anuncio.tfno = "SI"
    anuncio.mail = "NO"
    check_ep = request.POST.get("cep", False)
    if check_ep == "ep_on":
        anuncio.mail = "SI"
    try:
        anuncio.foto = request.FILES["foto"]
    except:
        pass
    categoria = models.Categoria.objects.get(pk = request.POST["categoria_id"])
    anuncio.categoria = categoria
    anuncio.save()
    return listado_usuario(request)

def borrar_anuncio(request):
    id_borrar = request.GET["id"]
    anuncio = models.Anuncio.objects.get(pk = id_borrar)
    imagen = str(anuncio.foto)
    noperfil = "images/profile/noperfil.png"
    if imagen != noperfil:
        try:
            os.remove("/home/particulariadj/portal_django/partdapp/static/media/"+imagen)
        except:
            pass
    models.Anuncio.objects.get(pk = id_borrar).delete()
    return listado_usuario(request)

def logout(request):
    request.session.clear()
    return listado(request)

def alta_usuario(request):
    nom = request.POST["nom"]
    apell = request.POST["apell"]
    nombre_ind = nom+" "+apell
    email_ind = request.POST["email"].lower().strip()
    clave_ind = request.POST["clave"]
    res = models.Usuarios.objects.filter(email = email_ind)
    if len(res) == 1:
        context = {
                "error_email" : "Ya hay un usuario con ese e-mail."
            }
        return render(request, "alta-login.html", context)
    else:
        codigo_gen = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        usuario = models.Usuarios(nombre = nombre_ind, email = email_ind, clave = clave_ind, codigo = codigo_gen)
        usuario.save()
        id_user = usuario.id
        correo = email_ind
        context = {
            "correo" : correo
            }
        mensaje = "<p>Muchas gracias por registrarte, "+nom+".<br><br><a style='color:green;' href='http://particulariadj.pythonanywhere.com/validar-alta?id={}&code={}';>Pincha aquí para finalizar el alta<a/></p><br><p><img src='http://particulariadj.pythonanywhere.com/static/images/mail.jpg'/></p>".format(str(id_user), str(codigo_gen))
        try:
            send_mail(
                'PARTICULARIA. Confirmación de alta.',
                '',
                'web.particularia@gmail.com',
                [usuario.email],
                fail_silently = False,
                html_message = mensaje)
        except Exception as e:
            error = str(e)
        return render(request,"altaok.html", context)

def validar_alta(request):
    id_a_validar = request.GET["id"]
    codigo_a_validar = request.GET["code"]
    resultado = list(models.Usuarios.objects.values_list('id').filter(id = id_a_validar, codigo = codigo_a_validar))
    if not resultado:
        return HttpResponse("ERROR: codigo de validacion incorrecto.")
    if resultado:
        usuario = models.Usuarios.objects.get(pk = id_a_validar)
        usuario.altavalida = "SI"
        usuario.save()
        return render(request, "validacionaltaok.html")

def grabar_anuncio(request):
    error = ""
    nom = request.POST["nom"]
    apell = request.POST["apell"]
    nombre_ind = nom+" "+apell
    if not validadores.validar_texto(nombre_ind):
        return "El nombre introducido es incorrecto"
    categoria_id = request.POST["materia"]
    descripcion_ind = request.POST["descripcion"]
    check_am = request.POST.get("am", False)
    check_pm = request.POST.get("pm", False)
    if check_am == "on" and check_pm == "on":
        horario_ind = "Mañana y tarde"
    elif check_am == "on":
        horario_ind = "Mañanas"
    elif check_pm == "on":
        horario_ind = "Tardes"
    telefono_ind = request.POST["telefono"]
    if not validadores.validar_telefono(telefono_ind):
        return "El telefono introducido es incorrecto"
    email_ind = request.POST["email"]
    if not validadores.validar_email(email_ind):
        return "El e-mail introducido es incorrecto"
    precio_ind = request.POST["precio"].replace(",",".")
    if not validadores.validar_precio(precio_ind):
        return "El precio por hora introducido es incorrecto"
    tfno_ind = "NO"
    check_tp = request.POST.get("ctp", False)
    if check_tp == "tp_on":
        tfno_ind = "SI"
    mail_ind = "NO"
    check_ep = request.POST.get("cep", False)
    if check_ep == "ep_on":
        mail_ind = "SI"
    foto_ind = "images/profile/noperfil.png"
    try:
        foto_ind = request.FILES["foto"]
    except Exception as e:
        error = str(e)
    codigo = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    categoria = models.Categoria.objects.get(pk = categoria_id)
    usuario = models.Usuarios.objects.get(pk = request.session["id_usuario"])
    anuncio = models.Anuncio(nombre = nombre_ind, descripcion = descripcion_ind, horario = horario_ind, telefono = telefono_ind, email = email_ind, precio = precio_ind, tfno = tfno_ind, mail = mail_ind, foto = foto_ind)
    anuncio.categoria = categoria
    anuncio.usuario = usuario
    anuncio.codigo = codigo
    anuncio.save()
    id_generado = anuncio.id
    codigo = anuncio.codigo
    correo = anuncio.email
    context = {
        "correo" : correo
        }
    mensaje = "<p>Muchas gracias por tu registro, "+nom+".<br><br><a style='color:green;' href='http://particulariadj.pythonanywhere.com/validar-anuncio?id={}&code={}';>Pincha aquí para validar el anuncio<a/></p><br><p><img src='http://particulariadj.pythonanywhere.com/static/images/mail.jpg'/></p>".format(str(id_generado), str(codigo))
    try:
        send_mail(
            'PARTICULARIA. Gracias por registrar tu anuncio.',
            '',
            'web.particularia@gmail.com',
            [anuncio.email],
            fail_silently = False,
            html_message = mensaje)
    except Exception as e:
        error = str(e)
    return render(request, "registrook.html", context)

def validar_anuncio(request):
    id_a_validar = request.GET["id"]
    codigo_a_validar = request.GET["code"]
    resultado = list(models.Anuncio.objects.values_list('id').filter(id = id_a_validar, codigo = codigo_a_validar))
    if not resultado:
        return HttpResponse("ERROR: codigo de validacion incorrectos.")
    if resultado:
        anuncio = models.Anuncio.objects.get(pk = id_a_validar)
        anuncio.emailvalido = "SI"
        anuncio.save()
        return render(request, "validacionok.html")

def form_contacto(request):
    nombre = request.GET.get("nombre")
    descripcion = request.GET.get("descripcion")
    email = request.GET.get("email")
    if request.GET.get("telefono"):
        telefono = request.GET.get("telefono")
    else:
        telefono = "No facilitado"
    nombre_lista = nombre.split()
    nombre_email = nombre_lista[0]
    mensaje = "<p>Mensaje recibido de {}<br><br>- Datos de contacto:<br>E-mail: {}<br>Teléfono: {}<br><br>- Mensaje:<br>{}".format(nombre, email, str(telefono), descripcion)
    error = ""
    try:
        send_mail(
            'MENSAJE DE CLIENTE',
            '',
            'web.particularia@gmail.com',
            ['web.particularia@gmail.com'],
            fail_silently = False,
            html_message = mensaje)
    except Exception as e:
        error = str(e)
    mensaje_resp = "<p>Gracias por contactar con nosotros, "+nombre_email+".<br><br>Hemos recibido tu mensaje correctamente y lo atenderemos lo antes posible.<br><br>Un saludo del equipo de <a style='color:green;' href='http://particulariadj.pythonanywhere.com';>Particularia<a/></p><br><p><img src='http://particulariadj.pythonanywhere.com/static/images/mail.jpg'/></p>"
    try:
        send_mail(
            'PARTICULARIA. Hemos recibido tu mensaje',
            '',
            'web.particularia@gmail.com',
            [email],
            fail_silently = False,
            html_message = mensaje_resp)
    except Exception as e:
        error = str(e)
    return render(request, "contactook.html")

def registrar_mensaje(request):
    nom_intr = request.GET["n"]
    mensaje_intr = request.GET["m"]
    mens = models.Chat(nom = nom_intr, mensaje = mensaje_intr)
    mens.save()
    return "ok"

def obtener_mensajes(request):
    mensajes = list(models.Chat.objects.values_list('nom', 'mensaje'))
    return JsonResponse(mensajes, safe=False)


