from django.shortcuts import render
from .forms import RegistForms1,RegistForms2
from django.http import HttpResponse

# Create your views here.

def regiser(request):

    if request.method=='POST':
        user_form=RegistForms1(request.POST)
        detail_form=RegistForms2(request.POST)

        if user_form.is_valid() and detail_form.is_valid():

            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['pw1'])
            new_user.save()

            new_detail=detail_form.save(commit=False)
            new_detail.username=new_user
            new_detail.save()
            return HttpResponse("Successful....")
        else:
            return HttpResponse('You cannot register...')
    else:
        user_form = RegistForms1(request.POST)
        detail_form = RegistForms2(request.POST)
        return render(request,'account/register.html',{'user_form':user_form,'detail_form':detail_form})