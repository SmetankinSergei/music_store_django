from random import choice

from django import template

from blog.models import Article

register = template.Library()


@register.simple_tag()
def get_published_articles():
    articles = Article.objects.all()
    result_set = set()
    while len(result_set) < 3:
        result_set.add(choice(articles))
    return result_set
