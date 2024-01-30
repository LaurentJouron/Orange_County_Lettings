from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404, handler500
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
]

# Pour la gestion des erreur 404 : page non trouvée
handler404 = views.handler404
# Pour la gestion des erreurs 500 (interne au serveur)
handler500 = views.handler500

# Added static URLs for media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
