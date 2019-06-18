#!/usr/bin/env python3

import requests
import os
import mdmail
from mailer import SendViaMail

class TopPosts():
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.retrive_posts()
    
    def retrive_posts(self):
        headers = {'User-Agent': 'RedditTopPosts'}
        url = "https://www.reddit.com/r/%s/top/.json?t=day.json" % self.subreddit
        posts = requests.get(url, headers=headers).json()
        self.top_posts = posts['data']['children']

class BeautifyTopPosts():
    
    def __init__(self, subreddit, top_posts):
        self.subreddit = subreddit
        self.top_posts = top_posts

    def markdown(self):
        message = "# %s \n" % self.subreddit
        message += "\n"
        for post in self.top_posts:
            message += "* [%s](https://reddit.com/%s)\n" % (post['data']['title'], post['data']['permalink'])
        return message        



if __name__ == '__main__':
    for sub in ['netsec', 'devops']:
        tp = TopPosts(sub)
        bp = BeautifyTopPosts(sub, tp.top_posts)
        SendViaMail(
            from_addr = "Reddit Top Posts <rtp@alorenzi.eu>",
            to_addr = "alorenzi@alorenzi.eu",
            subj =  "[%s] Reddit Top Posts" % sub,
            message_text= bp.markdown()
        )