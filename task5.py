import requests
from bs4 import BeautifulSoup # type: ignore
import csv

# Make a request to the website
r = requests.get('http://books.toscrape.com/')

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Find all the product containers
products = soup.find_all('article', class_='product_pod')

# Open the CSV file
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Name', 'Price', 'Rating'])

    # Loop through each product and scrape the name, price and rating
    for product in products:
        name = product.find('h3').find('a')['title']
        price = product.find('p', class_='price_color').text[1:]
        rating = ' '.join(product.find('p')['class'])

        # Write the data to the CSV
        writer.writerow([name, price, rating])

print("Data scraped and saved to products.csv")
