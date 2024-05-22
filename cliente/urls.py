from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('cliente/detalhe/<int:pk>/', views.detalhe, name="detalhe"),
    path('cliente/edit/<int:pk>/', views.edit, name="edit"),
    path('cliente/update/<int:pk>/', views.update, name="update"),
    path('cliente/delete/<int:pk>/', views.delete, name="delete"),
    path('cliente/form/', views.form, name='form'),
    path('cliente/create/', views.create, name='create'),
    path('cliente/dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)