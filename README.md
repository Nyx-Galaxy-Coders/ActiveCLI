# ActiveCLI
A little tool to make the visual part of creating CLI's a piece of cake

## How does it work?
It's surprisingly simple, just import it inside your script, and you're good to go!

## Features

* Colored printing, with similar syntax to Python's built in ``print()`` command

![image](https://user-images.githubusercontent.com/114549101/202034203-411cbae2-ccb0-4ae1-aff3-858c2a347d87.png)
* A divider... no need to copy the silly simbol, we got you!

![image](https://user-images.githubusercontent.com/114549101/202051841-9c7d402c-312f-4490-a1f5-ed498d00d39f.png)
* A Header... same thing but with text in the middle... and can be colored individually from the divider.

![image](https://user-images.githubusercontent.com/114549101/202051723-19dc20e5-9a5d-465f-8019-10c4011dcd3f.png)
* Pop-ups, so you can annoy your users :D

![image](https://user-images.githubusercontent.com/114549101/202051932-1fe1209d-7da4-472f-98a9-a3c5a56ca9f5.png)
* An easy universal-ish way of clearing the console.
* Loading animations, so you can halt... with style B)

![0a59f21c0f3b72aeea3bd47367fa664d](https://user-images.githubusercontent.com/114549101/202048951-a4227037-0a60-43b7-9500-1875adfda1fb.gif)


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
