from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('create/', views.ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='delete'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article'),
]
