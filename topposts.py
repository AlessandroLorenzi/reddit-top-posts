import requests
import os

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
            message += "* [%s](https://reddit.com%s)\n" % (post['data']['title'], post['data']['permalink'])
        return message        
