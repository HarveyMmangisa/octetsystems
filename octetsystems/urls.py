
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
   # path('products/', views.products, name='products'),
  # path('products/<slug>/', views.product_detail, name='product_detail'),
   # Corrected line in urls.py
path('services/', include('services.urls', namespace='services')),
#    path('about/', views.about, name='about'),
 #   path('contact/', views.contact, name='contact'),
    path('cyber-security/', views.cyber_security, name='cyber_security'),
 #   path('register/', views.register, name='register'),
  #  path('login/', views.login, name='login'),
   # path('logout/', views.logout, name='logout'),
]

