from django.urls import path
from . import views



urlpatterns = [
    
    path('bk/', views.bkash, name= 'paymentone'),
    path('rk/', views.rocket, name= 'paymenttwo'),
    path('pays/', views.payment_method),
    path('fv/', views.func_view),
    path('cv/', views.cls_dd.as_view()),   #class base view
    path('tv/', views.FirstTV.as_view()),  #class base Template view
    path('rv/', views.RedirectView.as_view(url = '/pay/tv')),   #class base Redirect view
    path('ddc/', views.RedirectView.as_view(url = '/pay/bk')),   #class base Redirect view
    path('ext/', views.externalRedirect.as_view())
            
    

]