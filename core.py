import tweepy
import pandas as pd
from natto import MeCab
import random
import threading
import time

from config import AK, ASK, AT, ATS

auth = tweepy.OAuthHandler(AK, ASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)
tweet_date = []
Twitter_ID = '@ihcamonoihS'

class Listener:
    def __init__(self):
        pass

    def liseten(self):
        count = 0

        for tweet in tweepy.Cursor(api.user_timeline, screen_name=Twitter_ID, exclude_replies=True).items():
            tweet_date.append([tweet.text])
            df = pd.DataFrame(tweet_date)

            count += 1

            if count == 5000:
                break

        return df

class CsvReader:
    def __init__(self):
        self.tweet_data = pd.DataFrame()

    def read_as_df(self, path):
        tweet_data = pd.read_csv(path)

        return tweet_data

    def read_as_ls(self, path):
        with open(path) as f:
            ls = list(f.read().split(','))

        text_ls = list(filter(lambda a: a != "", ls))

        return text_ls

class Analyser:
    def __init__(self):
        pass

    def disassembly(self, tweet_data: pd.DataFrame):
        nm = MeCab('-Owakati')
        first_word = []
        word_ls = []

        for i in range(len(tweet_date)):
            content = tweet_data.values[i].item()
            if '@' in content:
                pass
            elif '時報' in content:
                pass
            elif 'http:' in content:
                pass
            elif 'https:' in content:
                pass
            else:
                parsed_content = nm.parse(content)
                ls = list(parsed_content.split())
                if '\d' in ls[0] == False:
                    first_word.append(ls[0] + ',')

                word_ls.append(ls[1:])

        df_f = pd.DataFrame(first_word)
        df_w = pd.DataFrame(word_ls)

        df_f.to_csv('first_words.csv', index=False)
        df_w.to_csv('words.csv', index=False)

class Generate:
    def __init__(self):
        pass

    def marcov(self, text_ls):
        word_ls = text_ls
        markov_table = {}
        w1 = ''
        w2 = ''
        w3 = ''
        for word in word_ls:
            if w1 and w2 and w3:
                if (w1, w2, w3) not in markov_table:
                    markov_table[(w1, w2, w3)] = []
                markov_table[(w1, w2, w3)].append(word)
            w1, w2, w3 = w2, w3, word
        # 文章の自動作成
        count = 0
        sentence = ""
        w1, w2, w3 = random.choice(list(markov_table.keys()))

        n = range(100)
        while count < random.choice(n):
            tmp = random.choice(markov_table[(w1, w2, w3)])
            sentence += tmp
            w1, w2, w3 = w2, w3, tmp
            count += 1

        return str(sentence.strip())

    def JoinFirstWord(self, sentence, first_ls: list):
        JoinedSentence: str = random.choice(first_ls) + sentence
        Out_Sentence = JoinedSentence.replace('"', '').replace('\n', '')

        print(Out_Sentence)
        return Out_Sentence


listener = Listener()
analyser = Analyser()
reader = CsvReader()
generate = Generate()


def main():
    while True:
        text_ls = reader.read_as_ls('words.csv')
        first_ls = reader.read_as_ls('first_words.csv')

        sentence = generate.marcov(text_ls)
        tweet = generate.JoinFirstWord(sentence, first_ls)

        api.update_status(tweet)
        time.sleep(600)


def study():
    while True:
        df = listener.liseten()
        analyser.disassembly(df)
        time.sleep(18000)


if __name__ == '__main__':
    thread_1 = threading.Thread(target=main)
    thread_2 = threading.Thread(target=study)

    thread_1.start()
    thread_2.start()
