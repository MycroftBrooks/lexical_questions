import praw
import logging
logging.basicConfig(level = logging.INFO)

import re
"""import requests
import bs4 """
from decouple import config

from better_profanity import profanity

def reddit_parser(word_input, title_list):
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
            query=word_input, sort="hot", limit=30
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
                    for e in res:
                        title = title.replace(
                            e, f"<mark><span style='color:green'>{e}</span></mark>"
                        )
                    data = {"title": title}
                    title_list.append(data)
            else:
                continue
        