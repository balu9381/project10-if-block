from django.shortcuts import render

# Create your views here.
def ravi(request):
    d={'a':22}
    return render(request,'bala.html',d)