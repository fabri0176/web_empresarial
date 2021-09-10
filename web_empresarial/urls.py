
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),

    # Path admin
    path('admin/', admin.site.urls),
]

# Agregar cargar staticos en desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
