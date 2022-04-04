from django import views
import pyautogui
import time
from pynput.keyboard import Key,Controller as KeyboardController



keyboard= KeyboardController()

#import pyscreenshot
def screenshot(t1,vm):
    
    if t1==0:
        pyautogui.screenshot(r'C:\\Users\\manish1\\Desktop\\Screenshots\\'+vm+'_'+'imagefinal.png')
    else:
        
        for i in range(t1,0,-1):

            #i=i+1
            
            pyautogui.screenshot(r'C:\\Users\\manish1\\Desktop\\Screenshots\\'+vm+'_'+'image'+str(i)+'.png')
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
            #with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
                
            time.sleep(4)
        
        pyautogui.screenshot(r'C:\\Users\\manish1\\Desktop\\Screenshots\\image0.png')

#screenshot()