from django.db import models
from django.contrib.auth.models import User
import datetime



class aderezo(models.Model):
    nombre=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.nombre


class producto(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    descripcion= models.CharField(max_length=200,blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=50,blank=True, null=True)
    aderezo=models.ManyToManyField(aderezo,blank=True,null=True)
    imagen = models.ImageField( #es un archivo multimedia, solo guarda la ruta
    upload_to='productos',#donde lo voy a subir, 
    blank=True,
    null=True #https://docs.djangoproject.com/en/2.2/ref/models/fields/#null
    )

    def __str__(self):
        return self.nombre


class cliente(models.Model):
    nombre = models.CharField(max_length=20,blank=True, null=True)
    apellido= models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField()
    contacto = models.CharField(max_length=20,blank=True, null=True)
    cuenta_usuario=models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nombre


class producto_x_cliente(models.Model):
    producto=models.ForeignKey(producto, on_delete=models.CASCADE,blank=True, null=True)
    cliente=models.ForeignKey(cliente, on_delete=models.CASCADE,blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    direccion = models.CharField(max_length=30,blank=True,null=True)
    total = models.FloatField(blank=True, null=True)
    tiempo_cancelacion=models.TimeField(blank=True, null=True)
    expiro = models.BooleanField(default=False,blank=True, null=False)
    tiempo_estimado=models.CharField(blank=True,null=True,max_length=30)
    referencia=models.CharField(blank=True,null=True,max_length=200)

    def expiro_pedido(self):

        if self.tiempo_cancelacion > datetime.datetime.now().time():
            return True
        else:
            return False



    

    
class carrito(models.Model):
    productoC=models.ForeignKey(producto, on_delete=models.CASCADE,blank=True, null=True)
    clienteC=models.ForeignKey(cliente, on_delete=models.CASCADE,blank=True, null=True)

    def calcularElementos(self):
        return len(self.objects.all())
    

    






        








        









		


		