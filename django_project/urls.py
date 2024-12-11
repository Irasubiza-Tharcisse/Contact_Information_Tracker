
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('contacts.urls')),
    path('',include('account.urls')),
]
