from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'sivakumarreddy','age':23,'a':5,'b':9}
    return render(request,'wish.html',context=d)