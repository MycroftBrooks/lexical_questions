from django.contrib import admin
from .models import ChildQuestions, Test, Question

# Register your models here.
admin.site.register(ChildQuestions)


class QuestionInlineAdmin(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInlineAdmin]


admin.site.register(Test, TestAdmin)
