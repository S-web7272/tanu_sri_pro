from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from PIL import Image

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.google.com/search?q=computer+wallpaper+3d&tbm=isch&sxsrf=ALeKk03S7ybdvbir2biA9vS_EKPtfaNVow:1625807302021&source=lnms&sa=X&ved=2ahUKEwjr0NaVnNXxAhWk4nMBHblAC2gQ_AUoAXoECAEQAw&biw=1536&bih=754&dpr=1.25"
driver.get(url)
time.sleep(5)

# scrolling logic
curr_height = driver.execute_script("return document.body.scrollHeight")
print("page height:",curr_height)
for i in range(100): # number of time we scroll, increase it to scroll down more , meaning get more images
    driver.execute_script(f"window.scrollTo(0,{curr_height})")
    curr_height = driver.execute_script("return document.body.scrollHeight") # update the current height after scroll
    time.sleep(.5)   # wait for sometime
    print("page height updated:",curr_height)

# scroll ends here

images = driver.find_elements_by_css_selector("img.photo-item__img")
print("total images found:",len(images))

UPLOAD_DIR = "walpaper_imgs/"
for img in images:
    src =  img.get_attribute('src')
    # https://www.google.com/search?q=computer+wallpaper+3d&tbm=isch&sxsrf=ALeKk03S7ybdvbir2biA9vS_EKPtfaNVow:1625807302021&source=lnms&sa=X&ved=2ahUKEwjr0NaVnNXxAhWk4nMBHblAC2gQ_AUoAXoECAEQAw&biw=1536&bih=754&dpr=1.25
    filename = src.split("/")[-1]
    # pexels-photo-1319854.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
    filename = filename.split('?')[0]
    # pexels-photo-1319854.jpeg
    obj = requests.get(src, stream=True)
    Image.open(obj.raw).save(UPLOAD_DIR+filename) # load and save image to a folder
    print(f"image saved as {filename}")
driver.close()