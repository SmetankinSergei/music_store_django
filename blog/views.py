from django.db.models import F
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Article


class BlogListView(ListView):
    model = Article
    extra_context = {'title': 'blog'}


class ArticleCreateView(CreateView):
    model = Article
    fields = ['name', 'slug', 'content', 'img', 'is_published']
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'new article',
        'is_new_article': True,
    }

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['name', 'slug', 'content', 'img', 'is_published']
    extra_context = {
        'title': 'edit article',
        'is_update_article': True,
    }
    success_url = reverse_lazy('blog:blog')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog')


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {'title': 'article'}

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views_amount = F('views_amount') + 1
        article.save()
        return article
