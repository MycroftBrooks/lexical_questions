from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import RegisterUserFrom
import logging

logging.basicConfig(level=logging.INFO)


from .functions_python.child_parser_db import *
from .functions_python.reddit_parser import *
from .functions_python.cambridge_parser import *
from .models import ChildQuestions

title_list = []
dictionary_definition = []
dictionary_examples = []

# Adult section main page
def index(request):
    context = {
        "title_list": title_list,
        "dictionary_definition": dictionary_definition,
        "dictionary_examples": dictionary_examples,
    }
    if request.method == "POST":
        title_list.clear()
        dictionary_definition.clear()
        dictionary_examples.clear()
        word_input = str(request.POST["word_input"])
        cambridge_parser(word_input, dictionary_definition, dictionary_examples)
        reddit_parser(word_input, title_list)
        context = {
            "title_list": title_list,
            "word_input": word_input,
            "dictionary_definition": dictionary_definition,
            "dictionary_examples": dictionary_examples,
        }
        return render(request, "parser_app/index.html", context)
    else:
        return render(request, "parser_app/index.html")


def get_word_input(word_input):
    return word_input


# Child section
def child_questions(request):
    context = {
        "title_list": title_list,
    }
    if request.method == "POST":
        title_list.clear()
        word_input = str(request.POST["word_input"])
        child_parser_db(word_input, title_list)
        context = {"title_list": title_list, "word_input": word_input}
        return render(request, "parser_app/child_questions.html", context)
    else:
        return render(request, "parser_app/child_questions.html")


# Registarion page
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы зарегистрировались как " + username))
            return redirect("index")
    else:
        form = RegisterUserFrom()
    return render(request, "parser_app/register.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта"))
    return redirect("index")
