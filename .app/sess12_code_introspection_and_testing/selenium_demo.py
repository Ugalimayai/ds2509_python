# Python script to demonstrate opening a website and searching on google

# Ensure that selenium is installed by running: pip install selenium on the terminal

# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# set up the browser
driver = webdriver.Chrome() # Could also be firefox

# Open google
driver.get("https://google.com")

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for the result for 50s(allow us to fill in the captcha)
driver.implicitly_wait(50)

# Print/display the titles of the search results
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)

# Close the browser
driver.quit()
