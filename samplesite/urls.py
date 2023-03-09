from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bboard/', include('bbroad.urls')),
    path('admin/', admin.site.urls),
]
