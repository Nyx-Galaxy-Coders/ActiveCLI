import active_cli as ac
from active_cli import pcolor as print
from multiprocessing import freeze_support
from time import sleep
import webbrowser

def clear():
    ac.loading.stop()
    ac.clearconsole()

if __name__ == "__main__":
    freeze_support()
    if "yes" in ac.popup("Hey You!","You have been hacked, wanna check my Github? UwU",type=4):
        ac.popup("Thank you <3","You're the first one to say yes...")
    else:


        ac.popup("Y̷̧͍̯̻̫͈̗̔ͅô̵̺͕̲̦̣̰̩͙͜ư̸͙͉͎̱̫͚̻̭̮̺̔̅̈́́͆̾͌̉̃͛̀̕͘̚ ̵̡̦͍̫̙̪̪̖͎̙̞̪̀̓̾̔̈f̶̨̬̮̝̯̅̽̇͛̄̉͐̃̀̈́͜͠ͅơ̵̛̥̣͙͇͗̐̐̈́̈́̓͛͆̑͆̑o̶̢̧͎̘͚͗́̍̃̒̆͊̈́͊͋̈́̿̕̚ͅl̴̨̠̙̞̻̟̼̲̦͛͛̈́̓̈͜͝ͅ","YT̶̢̪̲̯̥̥͉̺̯̼̩͓̯̅̋̄̇̈́̈́͊͗͋̓̒̕̚͜ͅh̸͓͐̈̑͒͂͘̕e̶͖̜̼͖̳͍̗̟̬͔̞̩̔̈̿̄͗͂̓̏̇̓̓̆r̴̨̮̫̖̈́̓̑͌̉̄e̶̢̯͚̣̬̟͋͊͐̆̈́̅̉̈́̈́̾̽̽̏̐͘͜'̸̘̻̻̖̥̠̱͖̺̟̹̮͐́͌̓͑̍̓̉̏̿̋̒͆͜s̸͓̘̫̺̗̭͔̖̫̮̟̹͗̔̊̽̇̀͋̋̏̐̒͘͝ͅͅ ̵̨͙̹͋̔͗͋̒̌̕ṉ̸̨̛͉̣̭͈̳̟̥͑̈́̀̂̎͂͑ͅọ̴̢̼̦͔͙̲͈̙̜̿̒̚ ̶̧͙͖͎͔͔̼̗̩̀͜s̴̨̥̘̭̯̝̖͉̻̪͉̩̠͍̥͒̑͠c̴̛̩̘̥̭͋͛̈́͛̋̈́͜͜͝ͅą̴̞̤̌́p̵̧̙̠̠̘͎͐̌̋̏́̀̾͑̌̾̀͊̇͋̕e̷̡̞̻̻̭͔̐̈́͒̓̊̌̑̃̏̀̊̓͜͠")


    webbrowser.open("https://github.com/Nyx-Chan0-0")
    