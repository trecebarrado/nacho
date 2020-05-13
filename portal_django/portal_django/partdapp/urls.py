from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('registrar-anuncio', views.registro),
    path('contacto', views.contacto),
    path('listado', views.listado),
    path('contactar', views.contactar),
    path('grabar-anuncio', views.grabar_anuncio),
    path('validar-anuncio', views.validar_anuncio),
    path('alta-login', views.alta_login),
    path('alta-usuario', views.alta_usuario),
    path('validar-alta', views.validar_alta),
    path('login-usuario', views.login),
    path('listado-usuario', views.listado_usuario),
    path('logout-usuario', views.logout),
    path('editar-anuncio', views.editar_anuncio),
    path('borrar-anuncio', views.borrar_anuncio),
    path('guardar-cambios-anuncio', views.guardar_cambios_anuncio),
    path('form-contactar', views.form_contactar),
    path('form-contacto', views.form_contacto),
    path('registrar-mensaje', views.registrar_mensaje),
    path('obtener-mensajes', views.obtener_mensajes),
]
