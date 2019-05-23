from django.http import HttpResponse
from django.shortcuts import render
from .models import Question,Score
from account.models import People
import datetime
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def djadmin(request):
    return render(request,'djAdmin/index.html')

def randomChoiceQuestion(q,k=30):
    result=[]
    n=1
    while n<=k:
        que = random.choice(q)
        if not que in result:
            result.append(que)
            n+=1
    return result

@login_required(login_url='accounts/login/')
def checkexamtype(request,type):
    global examtype
    if type=='practice':
        examtype='practice'
        return HttpResponse(1)
    else:
        examtype='formal'
        return HttpResponse(0)



@login_required(login_url='accounts/login/')
def exam(request):

    today=datetime.datetime.today().date()
    people=People.objects.get(username=request.user) or None
    global qs
    if request.method=='GET':

        questions=[]

        ANS=['A','B','C','D','E']
        #展示试卷
        qs_all=Question.objects.all()
        qs=randomChoiceQuestion(qs_all,k=30)
        q_id=1
        for q in qs:
            s={}
            ans=q.option_set.all()
            s['q_t']=q.question
            s['id']='ans'+str(q_id)
            ans_={}
            for i in range(len(ans)):
                ans_[ANS[i]]=ans[i].option
            s['ans']=ans_
            questions.append(s)
            q_id+=1


        n = [i for i in range(1, len(questions) + 1)]

        return render(request, 'exam/exam.html', {'n': n,'questions':questions,'people':people,'today':str(today)})

    else:
        #检查答案并且提交分数

        print(examtype)

        score=0
        sub_ans=request.POST
        for i in range(30):
            ques_key='choiceans'+str(i+1)
            if ques_key in sub_ans.keys():
                if sub_ans[ques_key] == qs[i].rightAns:
                    score+=1

        s=Score()
        s.ansDate=datetime.datetime.today().date()
        s.ansType=examtype
        user=User.objects.get(username=request.user)
        s.user_id=user.pk
        s.score=score
        s.save()

        return render(request,'exam/result.html',{'user':user,'score':score})






