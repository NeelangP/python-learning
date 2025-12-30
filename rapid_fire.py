import pyautogui
import time

print("🔥 RAPID FIRE MODE LOADING...")
print("Switch to your game/app NOW.")
print("Starting in 5 seconds...")

time.sleep(5)

print("Firing")

for i in range(50):
    pyautogui.click()
    time.sleep(0.05)

print("Clip empty. Reloading")