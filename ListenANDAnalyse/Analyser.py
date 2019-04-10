from natto import MeCab
import pandas as pd

from ListenANDAnalyse.Listener import Listener
from config import path

class Analyser(Listener):
    def dissasembly(self, tweet_data: pd.DataFrame):
        nm = MeCab('-Owakati')
        first_word = []
        word_ls = []

        for t in range(len(tweet_data)):
            content = tweet_data.values[t].item()
            if '@' in content or '時報' in content or 'http' in content:
                pass
            else:
                parsed_content = nm.parse(content)
                ls = list(parsed_content.split())

                first_word.append(ls[0] + ',')
                word_ls.append(ls[1:])
        
        df_f = pd.DataFrame(first_word)
        df_w = pd.DataFrame(word_ls)

        df_f.to_csv(path['first_word'], index=False)
        df_w.to_csv(path['words'], index=False)

    def main(self):
        df = self.listen()
        self.dissasembly(df)
