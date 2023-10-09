"""
URL configuration for conociendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('pagina-nueva/', views.pagina_nueva, name="pagina_nueva"),
    path('saludo/', views.saludo, name="saludo"),
    path('saludo/<str:nombre>/', views.saludo, name="saludo"),
    path('redirecionar-index/', views.redireccionar_index, name="redireccionar"),
    path('index-template/', views.index_template, name="index_template"),
    path('hola-mundo-layout/', views.hola_mundo_layout, name="hola_mundo_layout"),
    path('herencia-contenido/', views.herencia_contenido, name="herencia_contenido"),
    path('crear-articulo/', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/', views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/', views.borrar_articulo, name="borrar_articulo"),
    path('filtrar-articulo/', views.filtrar_articulo, name="filtrar_articulo"),
    path('create-article/', views.create_article, name="create_article"),
    path('store-article/', views.store_article, name="store_article"),
    path('create-article-form/', views.create_article_form, name="create_article_form"),
    path('store-article-form/', views.store_article_form, name="store_article_form"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

    

