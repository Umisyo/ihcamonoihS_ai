from bunnsyo_seiseikunn import main as mn
from config import AK, ASK, AT, ATS
import tweepy
import time

auth = tweepy.OAuthHandler(AK, ASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth ,wait_on_rate_limit = True)

def Tweet():
    mn()
    api.update_status(sentence.strip())

while True:
    Tweet()
    time.sleep(60*15)

