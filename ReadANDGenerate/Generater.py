import random
from ReadANDGenerate.Reader import Reader
from config import path

class Generate(Reader):
    def __init__(self):
        pass

    def marcov(self, text_ls: list) -> str:
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

        return str(sentence)

    def JoinFirstWord(self, sentence: str, first_ls: list):
        JoinedSentence = random.choice(first_ls) + sentence
        Out_Sentence = JoinedSentence.replace('"', '').replace('\n', '')

        return Out_Sentence

    def main(self) -> str:
       words = self.read(path['words'])
       first_word = self.read(path['first_word'])

       sentence = self.marcov(words)
       tweet = self.JoinFirstWord(sentence, first_word)

       return tweet
