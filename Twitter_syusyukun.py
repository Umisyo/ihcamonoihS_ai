from config import AK, ASK, AT, ATS
import time
import pandas as pd
import tweepy

auth = tweepy.OAuthHandler(AK, ASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth ,wait_on_rate_limit = True)

tweet_data = []

def main():
    while True:
        count = 0

        for tweet in tweepy.Cursor(api.user_timeline,screen_name = '@ihcamonoihS',exclude_replies = True).items():
            tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])
            df = pd.DataFrame(tweet_data)
            print(df)
            df.to_csv('\\Users\\user\\awesome\\my_ai\\tweets.csv')
            count += 1

            if count == 100:
                break
        
        time.sleep(3600)

if __name__ == "__main__":
    main()