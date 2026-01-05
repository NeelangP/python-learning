import requests
from bs4 import BeautifulSoup
import csv
import time

print("STARTING CRAWLER...")

file = open('all_quotes.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["Quote", "Author"]) # Write the headers

for page_number in range(1, 6):
    url = f"http://quotes.toscrape.com/page/{page_number}/"
    print(f"Scraping Page {page_number}...")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    for i in range(len(quotes)):
        clean_quote = quotes[i].text.replace("“", "").replace("”", "")
        author = authors[i].text
        
        writer.writerow([clean_quote, author])
        
    time.sleep(1)

file.close()
print("DONE. Check 'all_quotes.csv' in your folder.")