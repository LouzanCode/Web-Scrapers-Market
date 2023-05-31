
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from registro import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('tienda.urls', namespace='tienda')), 
    path('carrito/', include('carrito.urls', namespace='carrito')), 
    path('registro/', v.registro, name='registro'),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #Configuración donde se guardaran las imagenes del proyecto en el lado del backend