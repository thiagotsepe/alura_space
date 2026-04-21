from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from galeria.models import Fotografia
from django.contrib import  messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias, "categoria_ativa": None})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)    
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})

def categoria(request, foto_categoria):
    fotografias = Fotografia.objects.filter(publicada=True, categoria=foto_categoria)
    return render(request, "galeria/index.html", {"cards": fotografias, "categoria_ativa": foto_categoria})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    buscar = request.GET.get("buscar")
    fotografias = Fotografia.objects.filter(publicada=True, nome__icontains=buscar)
    return render(request, "galeria/index.html", {"cards": fotografias})