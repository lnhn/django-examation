from django.shortcuts import render
from .forms import RegistForms1, RegistForms2
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import People
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def regiser(request):
    if request.method == 'POST':
        user_form = RegistForms1(request.POST)
        detail_form = RegistForms2(request.POST)

        if user_form.is_valid() and detail_form.is_valid():

            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['pw1'])
            new_user.save()

            new_detail = detail_form.save(commit=False)
            new_detail.username = new_user
            new_detail.save()
            return redirect(to='user_detail')
        else:
            return HttpResponse("你的用户名存在问题，请重新登录！")
    else:
        user_form = RegistForms1()
        detail_form = RegistForms2()
        return render(request, 'accounts/register.html', {'user_form': user_form, 'detail_form': detail_form})

@login_required(login_url='accounts/login/')
def student_home(request):
    user=User.objects.get(username=request.user)
    people=People.objects.get(username=user)
    return render(request,'accounts/profile.html',{'people':people})

