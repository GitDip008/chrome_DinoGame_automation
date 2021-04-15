import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

"""# Creating a rectangle to detect the position of a cactus
def draw():
    # for the cactus
    for i in range(170, 250):
        for j in range(430, 490):
            data[i, j] = 0

    # for the birds up
    for i in range(180, 200):
        for j in range(350, 390):
            data[i, j] = 100
"""


# Checking if the cactus collides with any black rectangle
# end here

def isCollide(data):
    """# for the birds up
    for i in range(230, 250):
        for j in range(350, 390):
            if data[i, j] < 20:  # if the part is black or near to black
                hit('down')
                return True
"""

    # for the cactus

    for i in range(385, 420):
        for j in range(430, 490):
            if data[i, j] < 20:  # if the part is black or near to black
                hit('up')
                return True

    for i in range(200, 250):
        for j in range(430, 490):
            if data[i, j] < 20:  # if the part is black or near to black
                hit('up')
                return True

    for i in range(155, 170):
        for j in range(430, 490):
            if data[i, j] < 20:  # if the part is black or near to black
                hit('up')
                return True

    return False


time.sleep(1)
while True:
    image = ImageGrab.grab().convert('L')       # taking a ScreenShot
    data = image.load()                         # loading the pixels as a 2D array
    isCollide(data)

# draw()
# image.show()

