import tweepy
from config import AK, ASK, AT, ATS
import time
import random

auth = tweepy.OAuthHandler(AK, ASK)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth ,wait_on_rate_limit = True)


def main():
    with open('/mnt/c/users/user/awesome/my_ai/tweets.txt') as f:
        text = f.read()

    dic = str.maketrans('','',"_/\.%~^|= []'()｢｣「」?？！!@.…：:,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ『』")

    wordlist = str(text.translate(dic))

    # マルコフ連鎖用のテーブルを作成する
    markov = {}
    w1 = ''
    w2 = ''
    w3 = ''
    for word in wordlist:
        if w1 and w2 and w3:
            if (w1, w2, w3) not in markov:
                markov[(w1, w2, w3)] = []
                #print('w1 not in markov ', w1)
                #print('w2 not in markov ', w2)
            markov[(w1, w2, w3)].append(word)
            #print('w1 append:', w1)
            #print('w2 append:', w2)
        w1, w2, w3 = w2, w3, word
        #print('w1:', w1)
        #print('w2:', w2)
    # 文章の自動作成
    count = 0
    sentence = ""
    w1, w2, w3 = random.choice(list(markov.keys()))

    N = range(100)
    while count < random.choice(N):
        tmp = random.choice(markov[(w1, w2, w3)])
        sentence += tmp
        w1, w2, w3 = w2, w3, tmp
        count += 1
    
    print(sentence.strip())
        
    #api.update_status(sentence.strip())
while True:
    main()
    #time.sleep(300)