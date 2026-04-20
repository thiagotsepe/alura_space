from django.urls import path
from galeria.views import index, imagem, categoria, buscar

urlpatterns = [
    path("", index, name="index"), 
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("categoria/<str:foto_categoria>/", categoria, name="categoria"),
    path("buscar/", buscar, name="buscar"),
]
