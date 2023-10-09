from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages
# Create your views here.

header = """<h1>Este es un sitio web para aprender Django | Cons Sorto</h1>
        <hr/>
        <h3>Menu</h3>
        <ul>
        <li>
           <a href="/">Inicio</a>
        </li>
        <li>
           <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
           <a href="/pagina-nueva">Pagina Nueva</a>
        </li>
        <li>
           <a href="/saludo/ConsSorto">Saludo</a>
        </li>
        <li>
           <a href="/redirecionar-index/">Redireccionar</a>
        </li>     
        <li>
           <a href="/index-template/">index con templates</a>
        </li>    
        <li>
           <a href="/hola-mundo-layout/">Hola Mundo Layout</a>
        </li>
        <li>
           <a href="/herencia-contenido/">Herencia Contenido Layout</a>
        </li> 
        </ul>
        <hr/>"""

def index(request):
    return HttpResponse(header+
        "<h1>Bienvenido a Django</h1>"+
        "<h3>esto es Django con CONS SORTO</h3>"
    )

def saludo(request, nombre = "Cons"):
    return HttpResponse(header+
        "<h1>Bienvenido a Django</h1>"+
        f"<h3>Saludos {nombre}</h3>"
    )

def hola_mundo(request):
    return HttpResponse(header+
        "<h1>Hola Mundo</h1>"+
        "<h3>Pagina de pruebas</h3>"
    )

def pagina_nueva(request):
    return HttpResponse(header+"""
        <h1>Nueva Pagina usando triple comilla para el html</h1>
        <h3>esta es otra pagina de pruebas</h3>
        """)

def redireccionar_index(request):
    return redirect("index")

def index_template(request):
    return render(request, "index_template.html")

def hola_mundo_layout(request):
    return render(request, "hola_mundo_layout.html")

def herencia_contenido(request):
    return render(request, "herencia_contenido.html")

def crear_articulo(request):
    articulo = Article(
        tittle = "Este es un nuevo articulo",
        content = "este es el contenido del articulo",
        public =1
    )

    articulo.save()

    return HttpResponse("articulo creado")

def articulo(request):
    articulo = Article.objects.get(pk=1, tittle = "Este es un nuevo articulo")
    return HttpResponse(f"articulo {articulo.tittle}")

def editar_articulo(request):
    articulo = Article.objects.get(pk=1)
    articulo.tittle = "articulo editado titulo"
    articulo.content = "articulo editado contenido"

    articulo.save()

    return HttpResponse(f"articulo {articulo.tittle}")

def articulos(request):
    articulos = Article.objects.all()
    
    return render(request, "articulos.html", {'articulos':articulos})

def borrar_articulo(request):
    articulo = Article.objects.get(pk=1)
    articulo.delete()

    return HttpResponse(f"articulo borrado")

def filtrar_articulo(request):
    articulo = Article.objects.filter(
        Q(tittle__contains = 'articulo') | Q(id = 1)
    )

    return render(request, "articulos.html", {'articulos':articulos})

def create_article(request):
    return render(request, "create_article.html")

def create_article_form(request):
    form_article = FormArticle()
    return render(request, "create_article_form.html", {'form':form_article})

def store_article_form(request):
    if request.method =='POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data
            tittle= data_form.get('tittle')
            content = data_form['content']
            public =data_form['public']

            if public == '1':
                public = True
            else:
                public = False

            article = Article(tittle = tittle,
                            content = content,
                            public = public)
            article.save()
            
            messages.success(request, f'se ha guardado el articulo id = {article.id}')
            
            return redirect("articulos")
        else:
            return render(request, "create_article_form.html", {'form':formulario})

"""
def store_article(request):
    if request.method =='GET':
        tittle= request.GET['tittle']
        content = request.GET['content']
        public =request.GET['public']

        if request.GET['public'] == 'on':
            public = True
        else:
            public = False

        article = Article(tittle = tittle,
                          content = content,
                          public = public)
        article.save()

        return redirect("articulos")
"""         
def store_article(request):
    if request.method =='POST':
        tittle= request.POST['tittle']
        content = request.POST['content']
        public =request.POST['public']

        if request.POST['public'] == 'on':
            public = True
        else:
            public = False

        article = Article(tittle = tittle,
                          content = content,
                          public = public)
        article.save()

        return redirect("articulos")
