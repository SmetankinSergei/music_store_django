from django import template

from blog.models import Article

register = template.Library()


@register.simple_tag()
def get_published_articles():
    return Article.objects.all()
