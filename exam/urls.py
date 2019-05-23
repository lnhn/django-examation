from django.urls import path
from .views import exam,checkexamtype

urlpatterns=[
    path('',exam,name='exam_index'),
    path('<type>',checkexamtype)
]