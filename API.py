import tweepy
from config import *

class API:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(AK, ASK)
    
    def main(self):
        self.auth.set_access_token(AT, ATS)
        api = tweepy.API(self.auth, wait_on_rate_limit=True)

        return api