from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from unique_id_generator import create_unique_id
import time
import json

# error handling
try:
    with open("products.py", "r") as file:
        products_json = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    products_json = []

"""Demoblaze.com"""
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

links = driver.find_elements(by = By.ID, value = 'itemc')
links[1].click()
# time.sleep(1)

next_button = driver.find_element(by = By.ID, value='next2')
next_button.click()
time.sleep(4)

soup = BeautifulSoup(driver.page_source, 'html.parser')

products = soup.find_all(class_ = 'col-lg-4 col-md-6 mb-4')
# print(products)
products_data = {}
for product in products:

    # scraping relevant data
    product_name = product.find_all(class_ = "hrefch")[0]
    # print(product_name.text)
    product_price = product.find_all('h5')[0]
    # print(product_price.text)
    product_desc = product.find_all(id = "article")[0]
    # print(product_desc.text)
    products_data[create_unique_id()] = {
        "laptop_name": product_name.text,
        "price": product_price.text,
        "desc": product_desc.text
    }

# saving all data
products_json.append(products_data)

with open("products.json", "w") as file:
    json.dump(products_json, file, indent = 4)