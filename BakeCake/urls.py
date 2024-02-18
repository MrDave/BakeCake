from django.contrib import admin
from django.urls import path, include
from cakes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main, name='main'),
    path('accounts/', include('phone_auth.urls')),
]
