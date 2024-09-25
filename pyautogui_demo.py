import pyautogui

import time



pyautogui.FAILSAFE=True




while True:
    time.sleep(0.5)

    try:
        
        
        target_pos=pyautogui.locateCenterOnScreen("target.png",confidence=0.7)
        # target_pos : the screen location that match the image 
        print(target_pos) 
        
    except:
        target_pos=None
        print('something went wrong..')
        continue
    else:
        print('nothing wrong yet')
        