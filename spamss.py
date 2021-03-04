import pyautogui, time
from time import sleep

##########
count = 0#
##########

while True:
    time.sleep(0)
    count += 1 
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Screenshot\screenshot{}.png'.format(count))