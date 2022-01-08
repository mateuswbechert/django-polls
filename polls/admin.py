from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    
admin.site.register(Question, QuestionAdmin)