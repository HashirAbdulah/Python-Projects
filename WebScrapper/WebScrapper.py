from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Logic for creating "Data" directory in webScrapper folder
path = r'C:\Users\M.Hashir Abdullah\Desktop\Python-Projects\WebScrapper'
dir = os.path.join(path, 'Data')

if not os.path.exists(dir):
    os.makedirs(dir)

try:
    driver = webdriver.Chrome()
    file = 0
    query = "mobiles"

    for i in range(1, 11): 
        try:
            logger.info(f"Navigating to page {i}")
            driver.get(f"https://www.daraz.pk/catalog/?page={i}&q={query}&spm=a2a0e.tm80335159.search.d_go")

            elems = driver.find_elements(By.CLASS_NAME, "qmXQo")
            print(f"{len(elems)} items found")
            
            for elem in elems:
                data = elem.get_attribute("outerHTML")
                filePath = os.path.join(dir, f"{query}-{file}.html")
                logger.info(f"Saving file to: {filePath}")
                with open(filePath, "w", encoding="utf-8") as f:
                    f.write(data)
                    file += 1
        
        except Exception as e:
            logger.error(f"Error on page {i}: {e}")

finally:
    driver.quit()
