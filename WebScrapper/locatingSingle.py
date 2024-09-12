from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
query = "mobiles"
driver.get(f"https://www.daraz.pk/catalog/?spm=a2a0e.tm80335159.search.d_go&q={query}")
elem = driver.find_element(By.CLASS_NAME, "qmXQo")
# print(elem.text)
print(elem.get_attribute("outerHTML"))

time.sleep(2)
driver.close()
