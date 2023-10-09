# Generated by Django 4.2.5 on 2023-10-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='', verbose_name='Imagen del articulo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='article',
            name='public',
            field=models.BooleanField(verbose_name='Esta publicado'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tittle',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='category',
            name='descripton',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
