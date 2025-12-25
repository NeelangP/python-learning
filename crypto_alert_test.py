import time
import winsound

# No requests import needed for this test
target_price = 100000 
print(f"Alert set for prices below ${target_price}")

# We will simulate a price dropping
fake_prices = [102000, 101000, 99000, 98000]

for price in fake_prices:
    print(f"Checking price: ${price:,}")
    
    if price < target_price:
        print("ALARM! Price is low!")
        # Beep at 1000Hz for 1 second
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
    else:
        print("Price is okay.")
        
    time.sleep(2) # Wait 2 seconds between fake checks