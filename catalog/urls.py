from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='catalog'),
    path('new_product/', views.ProductCreateView.as_view(), name='new_product'),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('show_category/', views.show_category, name='show_category'),
    path('show_my_products/', views.show_my_products, name='show_my_products'),
]
