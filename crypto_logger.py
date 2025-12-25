import requests
import time
import csv
from datetime import datetime

coin_id = "bitcoin"
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
filename = "bitcoin_history.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Price(USD)"])

print(f"Logging {coin_id} prices to {filename}...")

while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data[coin_id]['usd']

        now = datetime.now().strftime("%Y:%M:%D %H:%M:%S")

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now, price])
        
        print(f"Saved: {now} -> ${price}")
    else:
        print("Error fetching data")
    
    time.sleep(10)  