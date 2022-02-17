import random
import os

def locatemirrors():
    print('locatemirrors')
    for dir in os.listdir():
        if dir.endswith(".mirror"):
            print(dir)
