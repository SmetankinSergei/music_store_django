from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug', 'content', 'img', 'create_date', 'is_published', 'views_amount']
    prepopulated_fields = {'slug': ('name',)}
