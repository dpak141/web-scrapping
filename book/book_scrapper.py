import requests
from bs4 import BeautifulSoup
import csv

response = requests.get(url="https://books.toscrape.com/")

page_source = response.content

soup = BeautifulSoup(page_source, 'html.parser')
heading_elements = (soup.find_all('h3'))
pricing_element = soup.find_all('p', class_='price_color')


complete_data = []

for each_heading, each_pricing in zip(heading_elements, pricing_element):
    book_name = each_heading.text

    each_link = each_heading.find('a')
    book_link = each_link.get('href')

    book_price = each_pricing.get_text()

    complete_data.append(
        {'book_name': book_name, 'book_link': book_link, 'book_price': book_price})

csv_filename = 'scrape_book.csv'
fieldsNames = ['book_name', 'book_link', 'book_price']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv.DictWriter(csv_file, fieldnames=fieldsNames).writerows(complete_data)
