
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('gidieventapp/', include('gidieventapp.urls')),
    path('admin/', admin.site.urls),
]
