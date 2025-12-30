import pyautogui
import time

print("Click inside a text box (Notepad, Discord, Search Bar)...")
print("You have 5 seconds")

for i in range (5, 0, -1):
    print(i)
    time.sleep(1)

print("typing Now")

for i in range(10):
    pyautogui.write("Khel khtam hai lala")
    pyautogui.press("Enter")
    time.sleep(0.5)

print("Done")