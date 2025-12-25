import requests
import time

coin_id = input("Enter a coin name ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

print(f"Starting live tracker for {coin_id}....")
print("Press Ctrl + C to stop the program")

while True:

    response = requests.get(url)
    data = response.json()

    price = data[coin_id]['usd']

    print(f"{coin_id.capitalize}: ${price}")

    time.sleep(5)