from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'jinja_print.html',d)