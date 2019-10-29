from django.shortcuts import render
from django.shortcuts import redirect
from app_hamburguesa.models import *
from django.http import HttpResponse, HttpResponseRedirect
import json
from datetime import datetime,timedelta
import time
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


def registrar(request):

	if request.method == 'POST':
		nombre=request.POST['nombre']
		apellido=request.POST['apellido']
		contacto=request.POST['contacto']
		email=request.POST['email']
		contra=request.POST['contra']
		rep_contra=request.POST['rep_contra']
		try:
			usuario=User.objects.create_user(username=email,email=email,password=contra,first_name=nombre,last_name=apellido)
		except IntegrityError:
			#mensaje de error por duplicacion de usuario
			return redirect('principal')
		usuario.save()
		c=cliente(nombre=nombre,apellido=apellido,contacto=contacto,email=email,cuenta_usuario=usuario)
		c.save()
	return redirect('principal')

def log(request):
	#import pdb; pdb.set_trace() #permite ver que esta pasando
	if request.method == 'POST': 
		email=request.POST['email']
		password=request.POST['contra']
		user=authenticate(username=email,password=password) 
		if user:
			login(request,user)
			return redirect('principal')
		else:
			return render(request,'paginaError.html') 
	else:
		return render(request,'index.html')

def cerrarSesion(request):
	logout(request)
	return redirect('principal')


def principal(request):
	return render(request,"index.html")

def hamburguesa_simple(request):

	hamburguesa=producto.objects.filter(tipo="simple")
	titulo="HAMBURGUESAS SIMPLES"
	return render(request,"hamburguesas.html",{"titulo":titulo,"hamburguesa":hamburguesa,"tipo":True})


def hamburguesa_doble(request):
	hamburguesa=producto.objects.filter(tipo="doble")
	tipo="doble"
	titulo="HAMBURGUESAS DOBLES"
	return render(request,"hamburguesas.html",{"titulo":titulo,"hamburguesa":hamburguesa,"tipo":False})


def pedido(request):

	id=request.POST.get('id')
	prod=producto.objects.get(pk=id)
	lista_datos={'nombre_producto':prod.nombre,'tipo':prod.tipo,'precio':prod.precio}
	diccionario_json=json.dumps(lista_datos)
	return HttpResponse(diccionario_json)

def realizarpedido(request):

	if request.method == 'POST':

		direccion=request.POST['direccion']
		cantidad=request.POST['cantidad']
		id_producto=request.POST['id']
		p=producto.objects.get(pk=id_producto)
		c=cliente.objects.get(email=request.user.email)
		t=int(cantidad)*p.precio
		total=float(t)
		pxc=producto_x_cliente(producto=p,cliente=c,cantidad=cantidad,fecha=datetime.now(),hora=datetime.now().strftime('%H:%M:%S'),direccion=direccion,total=total)
		pxc.save()
		pxc.tiempo_cancelacion=pxc.fecha + timedelta(minutes=10)
		pxc.save()
	return redirect('pedidos')


def mispedidos(request):

	c = cliente.objects.get(email=request.user.email)
	pedidos=producto_x_cliente.objects.filter(cliente=c,fecha=datetime.now()).order_by('-hora')
	total=0
	for p in pedidos:
		total=total + p.total
	return render(request,"mispedidos.html",{"pedidos":pedidos,"total":total,"fecha_actual":datetime.now()})
		

def cancelarpedido(request):
	id_pedido=request.POST.get("id")
	producto_x_cliente.objects.get(pk=id_pedido).delete()
	return HttpResponse(True)

def carritos(request):

	cli=cliente.objects.get(email=request.user.email)
	c=carrito.objects.filter(clienteC=cli)
	return render(request,"carrito.html",{"carrito":c})

def addcarrito(request):
	
	id_producto=request.POST.get('id')
	p=producto.objects.get(pk=id_producto)
	c=cliente.objects.get(email=request.user.email)
	if carrito.objects.filter(productoC=p,clienteC=c).exists():
		return HttpResponse(False)
	else:	
		carrit=carrito(productoC=p,clienteC=c)
		carrit.save()
		return HttpResponse(True)

def eliminardelCarrito(request):
	
	id_producto=request.POST.get('id')
	p=producto.objects.get(pk=id_producto)
	c=cliente.objects.get(email=request.user.email)
	carrito.objects.get(productoC=p,clienteC=c).delete()
	return HttpResponse(True)

def nosotros(request):
	return render(request,"nosotros.html",{"usuario":True,"cantidad":cantidad})
