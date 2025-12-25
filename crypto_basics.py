import requests

# 1. Ask the user for the coin name
# .lower() converts "Bitcoin" to "bitcoin" because the API requires lowercase
coin_id = input("Enter the coin name (e.g., bitcoin, ethereum, solana): ").lower()

# 2. Inject the variable into the URL using an f-string
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

response = requests.get(url)
data = response.json()

# 3. Check if the coin actually exists in the data
if coin_id in data:
    price = data[coin_id]['usd']
    print(f"The price of {coin_id} is: ${price}")
else:
    print("Error: Coin not found. Make sure you typed the full name (e.g., 'ethereum' not 'eth').")