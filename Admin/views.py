from django.shortcuts import render


# Create your views here.
def TestFun(request):
    return render(request, 'LoginTemp.html')
