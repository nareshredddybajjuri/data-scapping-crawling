from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as Pd
 
excel = openpyxl.Workbook()

sheet = excel.active
sheet.title ='scrapped book data'

sheet.append(['Tile','Rating','Price','Availability'])


for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    source=requests.get(url)

    source = source.content

    soup = BeautifulSoup(source, 'html.parser')

    books = soup.find('ol', class_="row").find_all('article', class_="product_pod")
    for book in books:
        tag = book.find('h3')
        title = tag.find('a').attrs['title']
        star = book.find('p')
        rating = star['class'][1]
        price =book.find('p', class_="price_color").text
        price=float(price[1:])
        availability = book.find('p', class_="instock availability").text.strip()
        print(title, rating, price, availability)
        sheet.append([title, rating, price, availability])
        

excel.save('Scrapped_Book_Data.xlsx')
