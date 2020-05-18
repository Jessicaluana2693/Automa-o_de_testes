import webbrowser
import pyautogui
import time


webbrowser.open('https://www.trivago.com.br/')

time.sleep(9)

pyautogui.moveTo(630, 494, duration=0.25)
pyautogui.click(630, 494, button='left', duration=0.25)

time.sleep(3)

pyautogui.write('Natal', interval=0.25)
pyautogui.press('enter')

pyautogui.moveTo(1375, 494, duration=0.25)
pyautogui.click(1375, 494, button='left', duration=0.25)

time.sleep(3)

pyautogui.moveTo(1812, 381, duration=0.25)
pyautogui.click(1812, 381, button='left', duration=0.25)

time.sleep(3)

pyautogui.moveTo(1201, 171, duration=0.30)
pyautogui.click(1201, 171, button='left', duration=0.25)

time.sleep(3)

pyautogui.moveTo(1198, 226, duration=0.30)
pyautogui.click(1198, 226, button='left', duration=0.25)

time.sleep(3)

pyautogui.moveTo(617, 370, duration=0.25)
pyautogui.click(617, 370, button='left', duration=0.25)

time.sleep(3)

pyautogui.moveTo(603, 502, duration=0.25)
pyautogui.click(603, 502, button='left', duration=0.25)

time.sleep(5)

pyautogui.moveTo(775, 692, duration=0.25)
pyautogui.click(775, 692, button='left', duration=0.25)

time.sleep(2)

pyautogui.scroll(-12)

pyautogui.moveTo(660, 812, duration=0.25)
pyautogui.click(660, 812, button='left', duration=0.25)

pyautogui.scroll(-4)

time.sleep(3)

pyautogui.scroll(16)

pyautogui.moveTo(1348, 688, duration=0.35)
pyautogui.click(1348, 688, button='left', duration=0.30)
