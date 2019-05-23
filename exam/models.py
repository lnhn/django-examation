from django.db import models
from django.contrib.auth.models import User


class QuestionType(models.Model):
    questionType = models.CharField(max_length=5, verbose_name='题目种类')

    def __str__(self):
        return self.questionType


class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name='考试题目')
    examiner = models.ForeignKey(User, on_delete=models.CASCADE)
    questionType = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    rightAns = models.CharField(max_length=5, verbose_name='正确答案')

    def __str__(self):
        return self.question


class Option(models.Model):
    option = models.CharField(max_length=200, verbose_name='选项')
    question = models.ManyToManyField(Question, verbose_name='问题')

    def __str__(self):
        return self.option


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ansDate = models.DateField(verbose_name='答题日期')
    ansType = models.CharField(max_length=10, verbose_name='答题种类')
    score = models.CharField(max_length=3, verbose_name='分数')

    def __str__(self):
        return self.user.username
