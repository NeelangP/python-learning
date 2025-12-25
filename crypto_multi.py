import requests
import time
from datetime import datetime

coins_list = ["bitcoin", "ethereum", "solana"]

joined_ids = ",".join(coins_list)

url = f"https://api.coingecko.com/api/v3/simple/price?ids={joined_ids}&vs_currencies=usd"

print (f"tracking: {coins_list}")

while True:

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        now = datetime.now().strftime("%H:%M:%S")

        print("____________________")
        print(f"Update at [{now}]")

        for coin in coins_list:
            if coin in data:
                price = data[coin]['usd']
                print(f"{coin.capitalize()}: ${price:,}")
            else:
                print(f"{coin.capitalize}: data missing")

        print ("____________________")
        time.sleep(5)
    else:
        print(f"Error: {response.status_code}. Cooling down for 30 seconds...")
        time.sleep(30)