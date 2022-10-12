import pyautogui
import os
import Xlib.display
from time import sleep

from selenium import webdriver
from pyvirtualdisplay.smartdisplay import SmartDisplay

# for visible=1, install xserver-xephyr 
# otherwise, xfvb takes over 


display = SmartDisplay(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get( 'https://duckduckgo.com/' )
browser.save_screenshot( 'nrst.png' )
print(browser.title)

search = browser.find_element_by_id( 'search_form_input_homepage' )
search.send_keys( "Girish Parate From Sperentes Solution llp" )

# mouse moves in SmartDisplay 
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ[ 'DISPLAY' ])
try :
    x , y = pyautogui.locateCenterOnScreen( 'loupe.png' )
    pyautogui.moveTo(x , y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()
except :
    print("no magnifying glass found!")         

sleep(3)
browser.save_screenshot( 'auie.png' )
browser.quit ()

display.stop()




# import time
# from pyvirtualdisplay import Display
# from selenium import webdriver

# display = Display(visible=0, size=(1024, 768))
# display.start()

# browser = webdriver.Firefox()
# actions = webdriver.ActionChains(browser)
# browser.get('https://duckduckgo.com/')
# time.sleep(5) # sleep for 5 seconds
# content = browser.find_element_by_id('content')