from django.conf.urls import include, url
from django.contrib import admin
from app_hamburguesa.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'hamburguesa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', principal , name='principal'),
    url(r'^registro/', registrar ,name="registro"),
    url(r'^iniciarSesion/', log, name="login"),
    url(r'^cerrarSesion/', cerrarSesion, name="cerrarsesion"),
    url(r'^simple/', hamburguesa_simple , name='simple'),
    url(r'^doble/', hamburguesa_doble , name='doble'),
    url(r'^papas/', papas , name='papas'),

    url(r'^pedido/', pedido, name="pedido"),
    url(r'^realizarpedido/', realizarpedido ,  name="realizarP"),
    url(r'^mispedidos/', mispedidos , name="pedidos"),
    url(r'^cancelar/', cancelarpedido , name="cancelarpedido"),
    url(r'^carrito/', carritos , name="carrito"),
    url(r'^addcarrito/', addcarrito, name="addcarrito"),
    url(r'^delcarrito/', eliminardelCarrito , name="delcarrito"),
    url(r'^nosotros/', nosotros),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
