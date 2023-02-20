from django.contrib import admin
from .models import ChildQuestions, Test, Question, Bookpdf

# Register your models here.
admin.site.register(ChildQuestions)
admin.site.register(Bookpdf)


class QuestionInlineAdmin(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInlineAdmin]


admin.site.register(Test, TestAdmin)
