import active_cli as ac #Usually imported like that :)
from active_cli import pcolor as print
from time import sleep

ac.header(49,"Beeg brain quiz",color="cyan") #Header

print("If you get all questions correctly, your brain is huge!") # Little description
ac.breakline(2)

print("Are you ready to start? [Y/N]") # Actual content
i = input()

if "y" in i or "Y" in i: #Starting the "game"
    ac.clearconsole()
    ac.header(49,"Beeg brain quiz",color="cyan")
    ac.breakline(2)

    print("1. What's the programmer's worst enemy?",color="yellow")
    ac.breakline(1)
    print("A. Final User\nB. Boss\nC. Shitty coffee")
    i = input("")
    if i == "A" or i == "a":
        ac.clearconsole()
        ac.header(49,"Beeg brain quiz",color="cyan")
        ac.breakline(2)
        print("Nice!",color="cyan")
        sleep(1)
        
        ac.clearconsole()
        ac.header(49,"Beeg brain quiz",color="cyan")
        ac.breakline(2)
        
        print("2. What does YDC actually mean?\n",color="yellow")
        print("A. You don't care\nB. YouTube Downloader CLI\nC. You do care","cyan")
        i = input()
        if i == "A" or i == "a":
            ac.breakline(2) ; print("Get outta my head weirdo!",color="green") ; ac.breakline(2) ; print("Congratulations! your brain is huge",color="green")
        elif i == "B" or i == "b":
            ac.breakline(2) ; print("I guess someone was lurking trhough our Github... huh?") ; print("Congratulations! your brain is huge",color="green")
        elif i == "C" or i == "c":
            ac.breakline(2) ; print("You almost got it...",color="red")
        i = input()
    else: #Failing the "game"
        ac.breakline(2)
        print("You have a smol brain!",color="red")
        input()


else:
    print("Congrats! you won! (since you can't fail if you don't try)",color="green")
    input()
