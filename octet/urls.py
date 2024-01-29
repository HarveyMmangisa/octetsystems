from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', include(('services.urls', 'services'), views.services, name='services')),
    path('cyber-security/', views.cyber_security, name='cyber_security'),
    # Add other URL patterns as needed
]

