from django.shortcuts import render
from .models import Noticia
# Create your views here.
def noticias(request):
    noticias= Noticia.objects.all()
    return render(request,"noticias/noticias.html",{'noticias':noticias})