from django import template

from catalog.models import Product, Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.simple_tag()
def item_img_path_tag(item):
    return item.img.url


@register.filter()
def item_img_path(item_photo_path):
    return item_photo_path.url
