import tweepy
import pandas as pd
import API
from config import Twitter_ID

api = API.API()

class Listener:
    def __init__(self):
        self.Twitter_ID = Twitter_ID
        self.tweet_data = list()

    def listen(self) -> pd.DataFrame:
        count = 0
        for tweet in tweepy.Cursor(api.main().user_timeline, screen_name=self.Twitter_ID, exclude_replies=True).items():
            self.tweet_data.append([tweet.text])
            df = pd.DataFrame(self.tweet_data)

            count += 1

            if count == 5000:
                break

        return df