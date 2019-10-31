from django.contrib import admin
from	.models	import	*

class productoAdmin(admin.ModelAdmin):
	list_display=('nombre','descripcion','precio','stock')

class clienteAdmin(admin.ModelAdmin):
	list_display=('nombre','apellido','email','contacto')

class producto_x_clienteAdmin(admin.ModelAdmin):
	list_display=('cliente','producto','cantidad','direccion','referencia','fecha','hora','tiempo_cancelacion','total','tiempo_estimado')

class CarritoAdmin(admin.ModelAdmin):
	list_display=('productoC','clienteC')

		
admin.site.register(producto,productoAdmin)
admin.site.register(cliente,clienteAdmin)
admin.site.register(producto_x_cliente,producto_x_clienteAdmin)
admin.site.register(carrito,CarritoAdmin)
admin.site.register(aderezo)
