from django.contrib import admin
from django.urls import path, include

from cakes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main, name='main'),
    path('accounts/', include('phone_auth.urls')),
    path('api/create-order/', views.create_order, name="create-order"),
    path('api/form-data', views.form_data, name="form-data"),
    path('api/form-costs', views.form_costs, name="form-costs"),
]
