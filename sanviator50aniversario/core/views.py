from django.shortcuts import render, HttpResponse

contenido_html = """
<h1> Menu de navegación </h1>
<ul>
    <li><a href="/">Indice</a></li>
    <li><a href="/portfolio">Portfolio</a></li>
    <li><a href="/about">Sobre mi</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""
                 
    
# Create your views here.
def home(request):
    return render(request,"core/home.html")

def contact(request):
    
    return render(request,"core/contact.html")

def about(request):
    
    return render(request,"core/about.html")