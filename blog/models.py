from django.db import models


NULLABLE = {'blank': True, 'null': True}


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Article.Status.PUBLISHED)


class Article(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'draft'
        PUBLISHED = 1, 'published'

    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, **NULLABLE)
    content = models.TextField()
    img = models.ImageField(upload_to='articles_img/')
    create_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    views_amount = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-create_date',)
