from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
website_url = "https://en.wikipedia.org/wiki/main_page"

#load a website
driver.get(website_url)