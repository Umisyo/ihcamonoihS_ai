import threading
import time
from ListenANDAnalyse.Analyser import Analyser
from ReadANDGenerate.Generater import Generate
from API import API

analyse = Analyser()
generate = Generate()
api = API()

def posttweet():
    while True:
        api.main().update_status(generate.main())
        time.sleep(600)

def main():
    thread_1 = threading.Thread(target=posttweet)
    thread_2 = threading.Thread(target=analyse.main)

    thread_1.start()
    thread_2.start()

if __name__ == "__main__":
    main()