import html
import re

import praw
from better_profanity import profanity
from decouple import config
from django.shortcuts import render

title_list = []


def reddit_parser(word_input):
    reddit = praw.Reddit(
        client_id=config("client_id", default=""),
        client_secret=config("client_secret", default=""),
        user_agent=config("user_agent", default=""),
    )
    # ListOfBannedWords = ["nsfw", "sorry if", "reddit", "[serious]", "reddit", "redditor", "redditors", "reddit\'s"]
    if profanity.contains_profanity(word_input):
        title = "YOUR SEARCH CONTAINS PROFANITY"
        data = {"title": title}
        title_list.append(data)
    else:
        AskReddit_subreddit = reddit.subreddit("AskReddit").search(
            query=word_input, sort="hot"
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
        }
        for post in AskReddit_subreddit:
            if profanity.contains_profanity(post.title) == 0:
                mut = words & set(re.findall(r"(\w+)", post.title.casefold()))
                if len(mut) == 0:
                    w = word_input[0].lower()
                    w1 = word_input[0].upper()
                    word = f"\\b[{w}{w1}]{word_input[1:]}\\w?\\b"
                    title = post.title
                    res = re.findall(word, title)
                    print(res)
                    for e in res:
                        title = title.replace(
                            e, f"<span style='color:green'>{e}</span>"
                        )
                    data = {"title": title}
                    title_list.append(data)
            else:
                continue
        # print(title_list)


def index(request):
    context = {
        "title_list": title_list,
    }
    if request.method == "POST":
        title_list.clear()
        word_input = str(request.POST["word_input"])
        reddit_parser(word_input)
        context = {"title_list": title_list, "word_input": word_input}
        return render(request, "parser_app/index.html", context)
    else:
        return render(request, "parser_app/index.html")


def get_word_input(word_input):
    return word_input
