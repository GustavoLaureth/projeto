from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('detalhe/<int:pk>/', views.detalhe, name="detalhe"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)