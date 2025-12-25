import requests
import time
from datetime import datetime
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

coin_id = "bitcoin"
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
target_input = input("Alert me if Bitcoin drops below price: $")
target_price = int(target_input)

print(f"Monitoring {coin_id}.... Press Ctrl + C to stop")


while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data[coin_id]['usd']

        now = datetime.now().strftime("%H,%M,%S")
        print(f"[{now}] {coin_id}: ${price:,}")

        if price < target_price:
            print(">>> Alarm Triggered")

            message = (f"Alert! Bitcoin has dropped to {price} dollars")

            engine.say(message)
            engine.runAndWait()
    elif response.status_code == 429:
         print("Too many requests waiting for 60 seconds")
         time.sleep(60)
        
    else:
            print("Connection error")

    time.sleep(10)