"""e_commerce URL Configuration

"""

from django.urls import path
from .views import home_page, about_page, contact_page
from django.contrib import admin

urlpatterns = [
    path('', home_page),
    path('about/', about_page),
	path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
