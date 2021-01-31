import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin_url = os.environ.get("ADMIN_URL")

urlpatterns = [
    path(admin_url + '/', admin.site.urls),
    path('', include('House.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.TINYMCE_JS_URL, document_root=settings.TINYMCE_JS_ROOT)
