from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.carta_restaurante, name='carta_restaurante'),
    path('cargar_plato',views.cargar_plato,name='cargar_plato')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
