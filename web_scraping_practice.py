from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera%20dslr-mirrorless&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)

print(response.content)
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

print(soup.title.name)
#print(soup.prettify())