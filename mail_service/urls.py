from django.urls import path

from mail_service import views

app_name = 'mail_service'

urlpatterns = [
    path('', views.MailServiceListView.as_view(), name='mail_service'),
    path('mailing_details', views.MailingDetailView.as_view(), name='mailing_details'),
    path('create_mailing/<str:service_name>/', views.MailingCreateView.as_view(), name='new_mailing'),
    path('edit_mailing/<int:pk>/', views.MailingUpdateView.as_view(), name='edit_mailing'),
    path('delete_mailing/<int:pk>/', views.MailingDeleteView.as_view(), name='delete_mailing'),
    path('confirm_mailing', views.confirm_mailing, name='confirm_mailing'),
]
