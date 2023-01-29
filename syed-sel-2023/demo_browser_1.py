
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# invoking browser driver
# driver = webdriver.Chrome("C://Users//ipsbh//Desktop//syed-sel//syed-sel-2023//chromedriver.exe")
# serv_obj = Service("C://Users//ipsbh//Desktop//syed-sel//syed-sel-2023//chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()

# navigate to a url
driver.get("https://www.rahulshettyacademy.com/")

# maximize a window
driver.maximize_window()

# get title
title = driver.title

# validate title of the webpage
assert "Rahul Shetty Academy" in title, "title failed"

# get current_url of webpage
current_url = driver.current_url
print(current_url)

# navigate to a diff url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# navigate back
driver.back()

# refresh
driver.refresh()

# minimize_window
driver.minimize_window()

time.sleep(3) # only for debugging selenium code purposes
driver.close()
