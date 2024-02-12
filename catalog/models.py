from django.db import models
from django.db.models import PROTECT, CASCADE

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField()
    img = models.ImageField(upload_to='products_img/')
    category = models.ForeignKey('Category', on_delete=PROTECT, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=CASCADE, **NULLABLE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('change_published_status', 'Can change published status'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category'),
        ]


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{__class__.__name__}: {self.name}:product={self.product}:number={self.version_number}'

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
