from selenium import webdriver
from selenium.webdriver.common.by import By

# Starting a Selenium Webdriver session.
driver = webdriver.Chrome()

# Navigating to the web interface URL using an existing user id.
driver.get("http://127.0.0.1:5001/get_user_name/1")

# Checking that the username element is showing (web element exists).
driver.find_element(By.ID, value="user")

# Printing username (using locator).
element_locator = (By.ID, "user")
element = driver.find_element(*element_locator)
print("Element Text:", element.text)

driver.quit()
