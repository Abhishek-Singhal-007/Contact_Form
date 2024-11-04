from django.contrib import admin
from django.urls import path
from contact.views import contact_view, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_view, name='contact'),  # Contact form URL
    path('success/', success_view, name='success'),  # Success page URL
]
