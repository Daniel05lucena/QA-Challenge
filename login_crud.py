from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')


driver.get("http://localhost:3000/login")  


username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

username_input.send_keys("testuser")
password_input.send_keys("password")

password_input.send_keys(Keys.RETURN)

time.sleep(2)

assert "Dashboard" in driver.title 

driver.get("http://localhost:3000/products/new")

product_name_input = driver.find_element_by_name("productName")
quantity_input = driver.find_element_by_name("quantity")

product_name_input.send_keys("Apples")
quantity_input.send_keys("10")

submit_button = driver.find_element_by_name("submit")
submit_button.click()

time.sleep(2)

assert "Apples" in driver.page_source

driver.quit()

#NOTE: i've seen very little of automation in internet, that's what i could do it, I would appreciate a little more information on this topic, to do it perfectly.