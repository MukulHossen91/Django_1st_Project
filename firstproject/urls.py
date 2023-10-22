
from django.contrib import admin
from django.urls import path
from django.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay/', include('payments.urls')),
    path('pdc/', include('product.urls')),
    path('rvw/', include('review.urls')),
    
]