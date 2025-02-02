from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_options = Options()
# chrome_options.add_argument("--window-position=-1700, -200") #position window on the screen
# chrome_options.add_argument("--disable-popup-blocking")
# # Set up WebDriver (use the path to your driver if not in PATH)
# driver = webdriver.Chrome(chrome_options)

# # browser will remain open after the script ends
# chrome_options.add_experimental_option("detach", True) #didn't fully understand

# # open website
# driver.get("example.com")

# # print the page title
# print("Page title is: ", driver.title)

# # freeze time before quit
# time.sleep(10)

# # close the browser
# driver.quit()


driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/")
# search_box = driver.find_element(by = By.ID, value="tnb-google-search-input")
# search_box.send_keys("HTML")
# time.sleep(5)
# search_btn = driver.find_element(by = By.ID, value="tnb-google-search-submit-btn")
# search_btn.click()

# time.sleep(20)

# driver.quit()


"""Google search"""
# driver.get("https://www.google.com/")
# search_box = driver.find_element(by = By.ID, value = "APjFqb")
# search_box.send_keys("Restaurants near me" + Keys.ENTER)

# time.sleep(10)

# driver.quit()


"""Saucedemo.com"""
driver.get("https://www.saucedemo.com/")
search_box1 = driver.find_element(by = By.NAME, value="user-name")
search_box1.send_keys("problem_user")
time.sleep(3)

search_box2 = driver.find_element(by = By.NAME, value="password")
search_box2.send_keys("secret_sauce")
time.sleep(3)

submit_btn = driver.find_element(by = By.ID, value="login-button")
submit_btn.click()
time.sleep(10)

driver.quit()