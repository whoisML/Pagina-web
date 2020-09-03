from django.shortcuts import render
from django.utils import timezone
from .models import Post

#muestra la pagina de inicio
def inicio(request):
	pub = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('-fecha_de_publicacion')[:6]
	return render(request, 'blog/inicio.html', {'pub':pub})

#muestra las publicaciones del blog
def blog(request):
	pub = Post.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by('-fecha_de_publicacion')[:16]
	return render(request, 'blog/blog.html', {'pub':pub})

#muestra la publicacion seleccionada
def detalle_pub(request, pk):
	pub = Post.objects.get(pk=pk)
	return render(request, 'blog/detalle_pub.html', {'pub': pub})

def error_404(request, exception=None):
	return render(request,'blog/404.html', status=404)

def error_500(request):
	pass