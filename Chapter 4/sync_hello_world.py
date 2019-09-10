import time
from datetime import datetime


def say(what, delay):
    time.sleep(delay)
    print(what)

start = datetime.now()
say('first hello world', 100)
say('second hello world', 1)
say('third hello world', 4)
finish = datetime.now()
print("Elapsed: " + str(finish - start))
