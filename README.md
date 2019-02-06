# Artificial-Intellegence-Bot
A bot built to play the popular computer game "Sushi Go Round"(Code in src folder).

(larger video with lower FPS can be found below) 
<a href="https://imgflip.com/gif/2t1e8y"><img src="https://i.imgflip.com/2t1e8y.gif" title="made at imgflip.com"/></a>

Step 1:
To begin, the ImageGrab and ImageOps modules are imported from the Python Imaging Library in order to capture the playing screen to extract valuable pixel data from. The coordinates for the top left pixel and bottom right pixel of the play screen are found to use as global references for the rest of the program to forsee potential advertizments moving the play screen, thus altering the positions clicked by the mouse.

Step 2:
The coordinates for various button on the play screen must be found to carry out further functions. The Win32api and Win32con modules are used to implement mouse clicking functions to facilitate the process.

Step 3:
Implementing the two most dense functions in makeFood() and buyFood() utilize the numpy module to deduce color values to allow the computer to detect inputs from the characters in the game. To identify the type of sushi a costomer requests, a box with dimensions of preset size is set around the sushi icon at each table. The sum of the RGB color values for all the pixels in this box will allow the bot to identify in makeFood() the type of sushi to make. These values are stored in a python dictionary.

In order to indicate to the computer when to buyFood(), a counter dictionary is updated as the bot makes food. Once idicated the computer will buy more food if the RGB value of the buy menu item is not grey(indicating there is not enough money to buy this item). At this point, the driver can run and play the game.

<a href="https://imgflip.com/gif/2t1fam"><img src="https://i.imgflip.com/2t1fam.gif" title="made at imgflip.com"/></a>
