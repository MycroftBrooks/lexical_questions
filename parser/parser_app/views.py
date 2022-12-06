import html
import re

import praw
from better_profanity import profanity
from decouple import config
from django.shortcuts import render
import logging
logging.basicConfig(level = logging.INFO)
import json
import requests
import bs4

from .models import ChildQuestions

title_list = []
dictionary_definition = []

def index(request):
    context = {
        "title_list": title_list,
        "dictionary_definition": dictionary_definition
    }
    if request.method == "POST":
        title_list.clear()
        dictionary_definition.clear()
        word_input = str(request.POST["word_input"])
        cambridge_parser(word_input)
        reddit_parser(word_input)
        context = {"title_list": title_list, "word_input": word_input, "dictionary_definition": dictionary_definition}
        return render(request, "parser_app/index.html", context)
    else:
        return render(request, "parser_app/index.html")


def get_word_input(word_input):
    return word_input


#Functions for parsing Reddit
def reddit_parser(word_input):
    reddit = praw.Reddit(
        client_id=config("client_id", default=""),
        client_secret=config("client_secret", default=""),
        user_agent=config("user_agent", default=""),
    )
    words = {
            "nsfw",
            "sorry if",
            "reddit",
            "serious",
            "reddit",
            "redditor",
            "redditors",
            "reddit's",
            "onlyfans",
    }
    if profanity.contains_profanity(word_input):
        title = "YOUR SEARCH CONTAINS PROFANITY"
        data = {"title": title}
        title_list.append(data)
    else:
        AskReddit_subreddit = reddit.subreddit("AskReddit").search(
            query=word_input, sort="hot"
        ) 
        for post in AskReddit_subreddit:
            if profanity.contains_profanity(post.title) == 0:
                mut = words & set(re.findall(r"(\w+)", post.title.casefold()))
                if len(mut) == 0:
                    w = word_input[0].lower()
                    w1 = word_input[0].upper()
                    word = f"\\b[{w}{w1}]{word_input[1:]}\\w?\\b"
                    title = post.title
                    res = re.findall(word, title)
                    """ print(res) """
                    for e in res:
                        title = title.replace(
                            e, f"<mark><span style='color:green'>{e}</span></mark>"
                        )
                    data = {"title": title}
                    title_list.append(data)
            else:
                continue
        # print(title_list)


#Functions for child section
def child_questions(request):
    context = {
        "title_list": title_list,
    }
    if request.method == "POST":
        title_list.clear()
        word_input = str(request.POST["word_input"])
        child_parser_db(word_input)
        context = {"title_list": title_list, "word_input": word_input}
        return render(request, "parser_app/child_questions.html", context)
    else:
        return render(request, "parser_app/child_questions.html")


def child_parser_db(word_input):
    words = {
        "nsfw",
        "sorry if",
        "reddit",
        "serious",
        "reddit",
        "redditor",
        "redditors",
        "reddit's",
        "onlyfans",
    }
    if profanity.contains_profanity(word_input):
        title = "YOUR SEARCH CONTAINS PROFANITY"
        data = {"question": title}
        title_list.append(data)
    else:
        ChildList = ChildQuestions.objects.filter(
            question__icontains=word_input
        )
        for sentence in ChildList:
            if profanity.contains_profanity(sentence.question) == 0:
                mut = words & set(re.findall(r"(\w+)", sentence.question.casefold()))
                if len(mut) == 0:
                    w = word_input[0].lower()
                    w1 = word_input[0].upper()
                    word = f"\\b[{w}{w1}]{word_input[1:]}\\w?\\b"
                    title = sentence.question
                    res = re.findall(word, title)
                    """ print(res) """
                    for e in res:
                        title = title.replace(
                            e, f"<mark><span style='color:green'>{e}</span></mark>"
                        )
                    data = {"title": title}
                    title_list.append(data)
            else:
                continue

#Functions for getting data from cambridge dictionary
def cambridge_parser(word_input):
    url = "https://dictionary.cambridge.org/dictionary/english-russian/"
    url = url + word_input
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    try:
        definition = soup.find("div", class_="def ddef_d db").text
        data = {"definition": definition}
        dictionary_definition.append(data)
        print('its ok')
    except AttributeError as err:
        print("No definition found")
    try:
        all_examples = soup.find('div', class_='degs had lbt lb-cm').findAll(lambda tag: tag.name == 'span' and tag.get('class') == ['deg']) # 
        print(len(all_examples))
        for el in all_examples:
            print(el.text)
    except AttributeError as err:
        print("No example found")
    