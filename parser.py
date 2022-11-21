import praw
from decouple import config

reddit = praw.Reddit(client_id= config("client_id", default=''), client_secret= config("client_secret", default=''), user_agent= config("user_agent", default=''))

AskReddit_subreddit  = reddit.subreddit('AskReddit').search('spider', limit=10)

f = open('AskReddit.txt', 'w')

for post in AskReddit_subreddit:
    f.write(post.title)
    f.write("\n")

f.close()
