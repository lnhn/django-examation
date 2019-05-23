from django.contrib import admin

from .models import QuestionType,Question,Option,Score

# Register your models here.

admin.site.register((Question,QuestionType,Option,Score))