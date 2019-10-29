from django.conf.urls import include, url
from django.contrib import admin
from app_hamburguesa.views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'hamburguesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', principal , name='principal'),
    url(r'^registro/', registrar),
    url(r'^iniciarSesion/', log),
    url(r'^cerrarSesion/', cerrarSesion),
    url(r'^simple/', hamburguesa_simple , name='simple'),
    url(r'^doble/', hamburguesa_doble , name='doble'),
    url(r'^pedido/', pedido),
    url(r'^realizarpedido/', realizarpedido ,  name="realizarP"),
    url(r'^mispedidos/', mispedidos , name="pedidos"),
    url(r'^cancelar/', cancelarpedido),
    url(r'^carrito/', carritos , name="carrito"),
    url(r'^addcarrito/', addcarrito),
    url(r'^delcarrito/', eliminardelCarrito),
    url(r'^nosotros/', nosotros),
]
