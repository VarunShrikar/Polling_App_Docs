from django.contrib import admin

from .models import Question,Choice

admin.site.site_header = "Polls Admin"
admin.site.index_title = "Welcome to Polls Admin Area"
admin.site.site_title = "Polls"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
