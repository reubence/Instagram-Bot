import praw, requests, re
from instabot import Bot
import shutil
import time
import datetime


# server = flask.Flask(__name__)
# app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)

reddit = praw.Reddit(client_id="iTiTXJKRMWkfdQ",
                     client_secret="-uuCM4bnl_9pVkiLyqiR20OCCX0",
                     password="reuben123",
                     user_agent="insta-bot",
                     username="reubence")

subreddit = reddit.subreddit("memes")

hot = subreddit.hot(limit = 100)

topics_dict = { "title":[], \
                # "score":[], \
                # "id":[], "url":[], \
                # "comms_num": [], \
                # "created": [], \
                # "body":[]
                }

caption = "Lol"
ids = []
ids_parsed = []
file = open('ids.txt',"a")
while True:
    print("true")
        # while datetime.datetime.now().strftime("%H:%M:%S")>="12:00:00":
    print("checks datetime")
    reddit = praw.Reddit(client_id="iTiTXJKRMWkfdQ",
                         client_secret="-uuCM4bnl_9pVkiLyqiR20OCCX0",
                         password="reuben123",
                         user_agent="insta-bot",
                         username="reubence")

    subreddit = reddit.subreddit("memes")

    hot = subreddit.hot(limit = 7)
    fileo = open("ids.txt")
    ids = fileo.readlines()
    for i in ids:
        ids_parsed.append(i.replace("\n", ""))
    for post in hot:
        if post.id not in ids_parsed:
            caption = post.title
            response = requests.get(post.url.encode('utf-8'), stream=True)
            with open('img.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            file.write("\n" +post.id + "\n")
            file.close()

            try:
                bot = Bot()
                bot.login(username="memes_byai",
                          password="reuben123")
                bot.upload_photo("img.png",
                                 caption="%s \n. \n. \n. \n. \n. \n. \nThis is an auto-generated post. The Image & Caption were chosen from r/memes. " % caption)
                time.sleep(1800)
                print("sleeping")
                # file.close()
            except:
                continue
                print("Can't post to IG")
        else:
            continue