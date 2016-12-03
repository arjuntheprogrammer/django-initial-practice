from django.contrib import admin

# Register your models here.
#from .models import Question

#admin.site.register(Question)

#from .models import Question
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']
    inlines = [ChoiceInline]

    
admin.site.register(Question, QuestionAdmin)
