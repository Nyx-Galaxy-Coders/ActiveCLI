import active_cli as ac
from active_cli import pcolor as print
from multiprocessing import freeze_support
from time import sleep

def clear():
    ac.loading.stop()
    ac.clearconsole()

if __name__ == "__main__":
    freeze_support()
    input()
    ac.clearconsole()
    ac.loading.start(1,"Here's your loading")
    sleep(1)
    clear()
    ac.loading.start(2,"And another one")
    sleep(1)
    clear()
    ac.loading.start(3,"And another one")
    input()