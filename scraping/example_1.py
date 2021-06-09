from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
website_url ='https://www.google.com/search'
#load a website
search_term = 'comics'
driver.get(website_url+'?q=' +search_term)  