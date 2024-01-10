from res.chiffrement import *
from res.dechiffrement import *
from res.net.net import *
import time

class run:

    key = "hello"
    key_split = list(key)
    word = "abcde"
    word_split = list(word)
    adds = 0

    duplice_start = []
    duplice_end = []

    letters = []
    
    def chiffrement(key_split=key_split,word_split=word_split,adds=adds):
        Chiffrement.DUPLICE(key_split,word_split,adds)

    def banner():
        time.sleep(0.3)
        print("\t▀█▀ █ █ █▀▀   █▀▀ █ █ █▀▄ █▀▀ █▀▄ █▀▄ █▀▀ █▀▄")
        time.sleep(0.3)
        print("\t █  █▀█ █▀▀   ▀▀█ █▀█ █▀▄ █▀▀ █ █ █ █ █▀▀ █▀▄")
        time.sleep(0.3)
        print("\t ▀  ▀ ▀ ▀▀▀   ▀▀▀ ▀ ▀ ▀ ▀ ▀▀▀ ▀▀  ▀▀  ▀▀▀ ▀ ▀")
        time.sleep(0.4)
        print("\t-------------{ By SuperSuper88 }-------------\n")
        time.sleep(0.5)

    def menu():
        time.sleep( 0.2) 
        print("\t 1 / Chiffrement")
        time.sleep( 0.2)
        print("\t 2 / Dechiffremen")
        time.sleep( 0.2)
        print("\t 3 / Comment ca marche? \n")
        time.sleep( 0.2)
