from django.contrib import admin
from django.urls import path, include
from cakes.views import show_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='main'),
    path('accounts/', include('phone_auth.urls')),
]
