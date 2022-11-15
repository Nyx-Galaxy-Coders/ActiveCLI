# ActiveCLI
A little tool to make the visual part of creating CLI's a piece of cake

## How does it work?
It's surprisingly simple, just import it inside your script, and you're good to go!

## Features

* Colored printing, with similar syntax to Python's built in ``print()`` command

![image](https://user-images.githubusercontent.com/114549101/202034203-411cbae2-ccb0-4ae1-aff3-858c2a347d87.png)
* A divider... no need to copy the silly simbol, we got you!
* A Header... same thing but with text in the middle... and can be colored individually from the divider.
* Pop-ups, so you can annoy your users :D
* An easy universal-ish way of clearing the console.
* Loading animations, so you can halt... with style B)

## Heads up about the loading animations!

You **will** need to use this:
```
from multiprocessing import freeze_support

if __name__ == "__main__:
  freeze_support()
  [ Insert Your Code Here ]
```
For the animations to work properly or at all.
We still have no clue of an workaround ``¯\_(ツ)_/¯``
