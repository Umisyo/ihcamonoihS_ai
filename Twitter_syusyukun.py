import time
import pandas as pd
import tweepy
from natto import MeCab

from config import AK, ASK, AT, ATS

auth = tweepy.OAuthHandler(AK, ASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweet_data = []


class Twitter_syusyukun:
    def syusyu(self, auth):
        self.count = 0

        for tweet in tweepy.Cursor(api.user_timeline, screen_name='@ihcamonoihS', exclude_replies=True).items():
            tweet_data.append([tweet.text.replace('\n', '')])
            self.df = pd.DataFrame(tweet_data, index=None, columns=None, dtype=None, copy=False)
            # print(self.df)
            self.count += 1

            if self.count == 1000:
                break


class mecab_owakatikun(Twitter_syusyukun, MeCab):
    def owakatikun(self):
        self.nm = MeCab('-Owakati')
        self.result = ''
        self.syusyu(auth)
        self.tweet_ls = self.nm.parse(str(self.df.values))
        i = len(self.tweet_ls)
        for h in range(i) :
            if '@' in str(self.tweet_ls[h]):
                h += 1
            elif '時報' in str(self.tweet_ls[h]):
                h += 1
            elif 'RT' in str ( self.tweet_ls [ h ] ) :
                h += 1
            else:
                self.result += self.tweet_ls[h]
                h += 1
        self.write_txt = ''.join(self.result)
        with open('/mnt/c/users/user/awesome/my_ai/tweets.txt', 'a') as f:
            f.write(str(self.write_txt) + '\n')
            f.close
        print(self.write_txt)


mok = mecab_owakatikun()
while True:
    mok.owakatikun()
    time.sleep(18000 * 24)
