from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include("Main.urls")),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns() # Add a pattern to static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add a Media ROOT