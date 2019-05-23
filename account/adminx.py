from .models import People,Major
import xadmin

from exam.models import QuestionType,Question,Option,Score


xadmin.site.register(People)
xadmin.site.register(Major)
xadmin.site.register(Question)
xadmin.site.register(QuestionType)
xadmin.site.register(Option)
xadmin.site.register(Score)