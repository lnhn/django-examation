from django.urls import path
from .views import regiser
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import student_home

login_form=LoginForm()

urlpatterns = [
    path('register/', regiser,name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", extra_context={'login_form':login_form}), name="user_login"),
    path('detail/', student_home,name='user_detail'),
    path('logout/',auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name="user_logout"),
]
