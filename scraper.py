import requests
from bs4 import BeautifulSoup

print ("Connecting to servers")

url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    print("Access Granted. \n")

    soup = BeautifulSoup(response.text , 'html.parser')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author_name =  authors[i].text

        print(f"Author: {author_name}")
        print(f"Quote: {quote_text}")
        print("-"*50)

else:
    print("Failed to connect")