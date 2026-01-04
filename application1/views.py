from django.shortcuts import render 
from application1.models import Users 
from application1.forms import Users_Form 
def Test_Case1(request):
    form=Users_Form()
    if request.method=="POST":
       form=Users_Form(request.POST)
       if form.is_valid():
           form.save() 
    context={'form':form}
    return render(request,"application1/S1.html",context)


