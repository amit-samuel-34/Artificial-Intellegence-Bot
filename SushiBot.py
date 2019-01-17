from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import os
import time
import win32con, win32api


# Globals
# ------------------
import Cord

x_pad = 186
y_pad = 219

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

sushiTypes = {2670:'onigiri',
              3143:'caliroll',
              2677:'gunkan',}

"""

All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
x_pad = 186
y_pad = 219
Play area =  x_pad+1, y_pad+1, 826, 700 
"""



#capture the screen from computer
def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)

    ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    return a


#left mouseclick
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")  # completely optional. But nice for debugging purposes.


#hold down mouseclick
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left Down')


#release mouseclick
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left release')


#sets the mouse to those coordinates
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


#gets the coordinates the mouse is on
def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


#passes all unimportant screens
def startGame():
    # location of first menu
    mousePos((319, 192))
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
        print
        'Making a caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print
        'Making a onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)

        time.sleep(1.5)

    elif food == 'gunkan':
        print
        'Making a gunkan'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

#folds mat after ingredients on mat
def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

#buys all the food at once
def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print
        'test'
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print
            'rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print
            'rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print
        'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print
            'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print
            'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print
            'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print
            'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print
                '%s is low and needs to be replenished' % i
                buyFood(i)

def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print
            'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print
            'sushi not found!\n sushiType = %i' % s1

    else:
        print
        'Table 1 unoccupied'

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print
            'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print
            'sushi not found!\n sushiType = %i' % s2

    else:
        print
        'Table 2 unoccupied'

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print
            'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print
            'sushi not found!\n sushiType = %i' % s3

    else:
        print
        'Table 3 unoccupied'

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print
            'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print
            'sushi not found!\n sushiType = %i' % s4

    else:
        print
        'Table 4 unoccupied'

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print
            'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print
            'sushi not found!\n sushiType = %i' % s5

    else:
        print
        'Table 5 unoccupied'

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print
            'table 1 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print
            'sushi not found!\n sushiType = %i' % s6

    else:
        print
        'Table 6 unoccupied'

    clear_tables()


def get_seat_one():
    box = (45, 427, 45 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_two():
    box = (146, 427, 146 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_three():
    box = (247, 427, 247 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_four():
    box = (348, 427, 348 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_five():
    box = (449, 427, 449 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_six():
    box = (550, 427, 550 + 63, 427 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print
    a
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a


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



class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041

#code to get cords without multiple calls in console
''' for i in range(6):
    time.sleep(1.2)
    print(get_cords())
'''
