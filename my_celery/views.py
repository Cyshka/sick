from django.shortcuts import render

from mysite.tasks import summ


# Create your views here.


def get_page(request):
    summ.delay(100,200)
    return render(request,'index.html')