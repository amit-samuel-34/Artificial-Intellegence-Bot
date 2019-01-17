# Artificial-Intellegence-Bot
A bot built to play the popular computer game "Sushi Go Round". An adaptation of Chris Kiehl's implementation.

Step 1:
To begin, the ImageGrab and ImageOps modules are imported from the Python Imaging Library in order to capture the playing screen to extract valuable pixel data from. The coordinates for the top left pixel and bottom right pixel of the play screen are found to use as global references for the rest of the program to forsee potential advertizments moving the play screen, thus altering the positions clicked by the mouse.

Step 2:
The coordinates for various button on the play screen must be found to carry out further functions. The Win32api and Win32con modules are used to implement mouse clicking functions to make the process less stressfull.
