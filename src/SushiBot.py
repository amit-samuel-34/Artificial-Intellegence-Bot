from PIL import ImageGrab, ImageOps
import win32con, win32api
from numpy import *
import os #navigate OS's directories
import time
import Cord

"""

All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
x_pad = 19
y_pad = 156
Play area =  x_pad+1, y_pad+1, 659, 636 
"""

# Globals
# ------------------

#Provides padding for all coordinates to improve adaptability
x_pad = 188
y_pad = 148

#Keeps track of the current number of each food
foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

#Sum of a sushi's color values within a bounding box
sushiTypes = {2670:'onigiri',
              3143:'caliroll',
              2677:'gunkan',}

#Helper class that keeps the sum of the blank box above where sushi icons are displayed
class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11596
    seat_4 = 10613
    seat_5 = 7286
    seat_6 = 9119


#capture the screen from computera
def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)

    return im

#grabs a bounded image and sums its color values
def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors()) #from PIL
    a = a.sum()
    print(a)
    return a

#left mouseclick
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    # print("Click.")  # completely optional. But nice for debugging purposes.

#hold down mouseclick
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    #print('left Down')

#release mouseclick
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    # print('left release')

#sets the mouse to those coordinates
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1])) #adjusts padding in function

#gets the coordinates the mouse is on
def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)



#passes all unimportant screens
def startGame():
    # location of first menu
    mousePos((319, 192)) #coord padding adjusted in mousePos
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((325, 388))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((574, 444))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((326, 376))
    leftClick()
    time.sleep(.1)

#clears empty plates
def clear_tables():
    mousePos((84, 210))
    leftClick()

    mousePos((195, 210))
    leftClick()

    mousePos((293, 210))
    leftClick()

    mousePos((387, 210))
    leftClick()

    mousePos((492, 210))
    leftClick()

    mousePos((594, 210))
    leftClick()
    time.sleep(1)

#makes certain sushi
def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.1)

        time.sleep(1.5)

    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

#folds mat after ingredients on mat
def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) #avoid clicking an ingredient
    leftClick()
    time.sleep(.1)

#buys all the food at once
def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.1)
        leftClick()
        time.sleep(.5) #time should not go below .5 seconds
        s = screenGrab() #Grabs only the playing screen so no pads are required
        time.sleep(.1)

        if s.getpixel(Cord.buy_rice) != (118, 83, 85): #Coord for rice icon greyed out
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(1.5)
        else:
            print('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food) #keep recurring until your account reaches the right amount

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        time.sleep(.5) #do not go below .5 sec
        s = screenGrab() #Grabs only the playing screen so no pads are required
        time.sleep(.1)

        #print(s.getpixel((Cord.noriX, Cord.noriY)))
        if s.getpixel(Cord.t_nori) != (33, 30, 11):#Coord for nori icon greyed out
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(1.5)
        else:
            print('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        time.sleep(.5) #time should not go below .5 seconds
        s = screenGrab() #Grabs only the playing screen so no pads are required
        time.sleep(.1)

        #print(s.getpixel((Cord.roeX, Cord.roeY)))
        if s.getpixel((Cord.t_roe)) != (101, 13, 13):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(1.5)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

#Checks to see if any food item is about to be depleted
#calls buyFood() if so
def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 3:
                print('%s is low and needs to be replenished' % i)
                buyFood(i)

#checks each seat bubble for customers
def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1: #checks if the sum of a seat's color pixels are that of a sushi
        if s1 in sushiTypes: #checks if the sum is a particular sushi
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print('sushi not found!\n sushiType = %i' % s1)

    else:
        print('Table 1 unoccupied')

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print('sushi not found!\n sushiType = %i' % s2)

    else:
        print('Table 2 unoccupied')

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print('sushi not found!\n sushiType = %i' % s3)

    else:
        print('Table 3 unoccupied')

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print('sushi not found!\n sushiType = %i' % s4)

    else:
        print('Table 4 unoccupied')

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print('sushi not found!\n sushiType = %i' % s5)

    else:
        print('Table 5 unoccupied')

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print('sushi not found!\n sushiType = %i' % s6)

    else:
        print('Table 6 unoccupied')

    clear_tables()

#finds the bounding box the customer's sushi display would be
def get_seat_one():
    box = (x_pad + 26, y_pad + 61, x_pad + 26 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))#screengrab is too specific, must use built-in grab.
    a = array(im.getcolors())                   #using grayscale sums the RBG values, and makes the process faster
    a = a.sum()
    return a

def get_seat_two():
    box = (x_pad + 127, y_pad + 61, x_pad + 127 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

def get_seat_three():
    box = (x_pad + 228, y_pad + 61, x_pad + 228 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

def get_seat_four():
    box = (x_pad + 329, y_pad + 61, x_pad + 329 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

def get_seat_five():
    box = (x_pad + 430, y_pad + 61, x_pad + 430 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

def get_seat_six():
    box = (x_pad + 531, y_pad + 61, x_pad + 531 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

#calls all get_seat methods
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()




#helper method for begugging
def get_seats_helper():
    startGame()
    for x in range(10):
        get_all_seats()
        print('\n')
        time.sleep(1.2)
#helper method for begugging
def makeCali():
    for x in range(6):
        makeFood('caliroll')

#code to get cords without multiple calls in console
''' for i in range(6):
    time.sleep(1.2)
    print(get_cords())
'''
