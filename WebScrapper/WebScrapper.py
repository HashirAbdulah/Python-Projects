# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# query = "mobiles"
# for i in range(1,3):
#     driver.get(f"https://www.daraz.pk/catalog/?page={i}&q={query}&spm=a2a0e.tm80335159.search.d_go")
#     elems = driver.find_elements(By.CLASS_NAME, "qmXQo")
#     # print(elems)
#     print(f"{len(elems)} items found")

#     for elem in elems:
#         print(elem.text)
#         # print(elem.get_attribute("outerHTML"))

#     time.sleep(2)
#     driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:

    driver = webdriver.Chrome()

    query = "mobiles"
    for i in range(1, 3):  
        try:
            logger.info(f"Navigating to page {i}")
            driver.get(f"https://www.daraz.pk/catalog/?page={i}&q={query}&spm=a2a0e.tm80335159.search.d_go")

            elems = driver.find_elements(By.CLASS_NAME, "qmXQo")
            print(f"{len(elems)} items found")
            
            logger.info(f"Page {i}: {len(elems)} items found")

            for elem in elems:
                print(elem.text)
            
            time.sleep(5)
        
        except Exception as e:
            logger.error(f"Error on page {i}: {e}")

finally:
    driver.quit()
