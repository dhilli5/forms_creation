from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    if request.method=="POST":
        name=request.POST["un"]
        password=request.POST['pw']
        return HttpResponse("insert data submited successfully")
    return render(request,'hello.html')