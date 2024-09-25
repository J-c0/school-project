'''
import cv2
import numpy
# import pyautogui  #1
from time import time
from PIL import ImageGrab

loop_time=time()

while True:
    screenshot=ImageGrab.grab()
    # screenshot=pyautogui.screenshot()  #1
    # take a screenshot
    screenshot=numpy.array(screenshot)
    # convert it to let cv2 understand the image
    screenshot=cv2.cvtColor(screenshot,cv2.COLOR_RGB2BGR)
    # convert the colour to bgr form 

    print('FPS:  ',1/(time()-loop_time))
    loop_time=time()
    cv2.imshow('computer vision',screenshot)


    if cv2.waitKey(10)==ord('r'):
        break

'''

import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture



# initialize the WindowCapture class
wincap = WindowCapture()
loop_time = time()
while(True):

    # get an updated image of the screen
    screenshot = wincap.get_screenshot()
    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
