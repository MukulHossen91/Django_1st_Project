from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from payments.models import pay_method
from django.views import View
from django.views.generic.base import TemplateView, RedirectView



# Create your views here.

def bkash(request):
    return render(request, 'payments/payments1.html')


def rocket(request):
    d = datetime.now()
    return render(request, 'payments/payments2.html')

    
def payment_method(request):
    pay_m = pay_method.objects.all()
    return render(request, 'payments/pay.html', {'pay' : pay_m})


#Fucntion based views
def func_view(request):
    return render(request, 'product/product.html')

#class based views
class cls_dd(View):
    def get(self, request):
        return render(request, 'product/product.html')
    

#Templet view
class FirstTV(TemplateView):
    template_name = 'payments/payments1.html'


#extarnel Redirect view
class externalRedirect(RedirectView):
    url = 'https://www.w3schools.com/'

   
    
    
    


 