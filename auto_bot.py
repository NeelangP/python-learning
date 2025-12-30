import pyautogui
import time

print("Script starting in 3 seconds... (Move mouse to corner to abort)")
time.sleep(3)

width , height = pyautogui.size()
print("Screen Resolution : {width} x {height}")

print("Drawing Square")
distance = 200

for i in range (4):
    pyautogui.moveRel(distance , 0 , duration=0.5)
    distance = distance - 20
    pyautogui.moveRel(0 , distance , duration=0.5)
    pyautogui.moveRel(-distance , 0 , duration=0.5)
    pyautogui.moveRel(0 , -distance , duration=0.5)

print("Done.")