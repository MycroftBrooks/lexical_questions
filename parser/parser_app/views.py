from django.shortcuts import render
import praw
from decouple import config



title_list=[]

def reddit_parser():
    reddit = praw.Reddit(client_id= config("client_id", default=''), client_secret= config("client_secret", default=''), user_agent= config("user_agent", default=''))
    AskReddit_subreddit  = reddit.subreddit('AskReddit').search('issue', limit=10)
    for post in AskReddit_subreddit:
        title = post.title
        data = {'title': title }
        title_list.append(data)
    print(title_list)

reddit_parser()


def index(request):
    context = {
        'title_list': title_list
    }
    return render(request, 'parser_app/index.html', context)

