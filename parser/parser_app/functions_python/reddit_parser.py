import praw
import logging
logging.basicConfig(level = logging.INFO)

import re
"""import requests
import bs4 """
from decouple import config

from better_profanity import profanity

def reddit_parser(word_input, title_list):
    """ url = f"https://www.reddit.com/r/AskReddit/search/?q={word_input}&restrict_sr=1&sr_nsfw=&sort=hot"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "html.parser") """
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
        """ try:
            all_titles = soup.find("div", class_="QBfRw7Rj8UkxybFpX-USO").findAll("h3", class_="_eYtD2XCVieq6emjKBH3m")
            #for el in all_titles:
                print(el.text)
                #data = {"title": el.text}
                #title_list.append(data)  
            for el in all_titles:
                el = el.text
                if profanity.contains_profanity(el) == 0:
                    print('its ok')
                    mut = words & set(re.findall(r"(\w+)", el.casefold()))
                    if len(mut) == 0:
                        w = word_input[0].lower()
                        w1 = word_input[0].upper()
                        word = f"\\b[{w}{w1}]{word_input[1:]}\\w?\\b"
                        res = re.findall(word, el)
                        for e in res:
                            el = el.replace(
                                e, f"<mark><span style='color:green'>{e}</span></mark>"
                            )
                        data = {"title": el}
                        title_list.append(data)
                    else:
                        continue
        except AttributeError as err:
            title = "NO RESULTS FOUND"
            data = {"title": title}
            title_list.append(data) """
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
        