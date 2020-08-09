import praw, requests, re
from instabot import Bot
import shutil
import time
# import dash
# import dash_auth
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# import flask


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
fileo = open("ids.txt")
ids = fileo.readlines()
for i in ids:
    ids_parsed.append(i.replace("\n",""))

print(ids)
print(ids_parsed)

file = open('ids.txt',"a")
while True:
    for post in hot:
        if post.id not in ids_parsed:
            caption = post.title
            response = requests.get(post.url.encode('utf-8'), stream=True)
            with open('img.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            file.write("\n" +post.id + "\n")
            try:
                bot = Bot()
                bot.login(username="memes_byai",
                          password="reuben123")
                bot.upload_photo("img.png",
                                 caption="%s \n. \n. \n. \n. \n. \n. \nThis is an auto-generated post. The Image & Caption were chosen from r/memes. " % caption)
            except:
                continue
                print("Can't post to IG")
            # print(post.id)
            # break
    print("sleeping")
    time.sleep(1000)
file.close()
