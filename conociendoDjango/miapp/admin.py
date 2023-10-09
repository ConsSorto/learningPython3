from django.contrib import admin
from .models import Article, Category
# Register your models here.

class ArticleReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')


admin.site.register(Article, ArticleReadOnlyFields)
admin.site.register(Category)

