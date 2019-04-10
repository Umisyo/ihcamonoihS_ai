import pandas as pd

class Reader:
    def __init__(self):
        pass

    def read(self, path) -> list:
        with open(path) as f:
            ls = list(f.read().split(','))

        text_ls = list(filter(lambda a:a != "", ls))

        return text_ls
        