import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# locate a name textbox
# id, name, class_name, link_text, partial_link_text, css_selector, xpath, tag_name
name_textbox = driver.find_element(By.NAME, "name")

# enter a text in name_textbox
name_textbox.send_keys("Selenium 4")

# clear the text
name_textbox.clear()

# locate the checkbox
checkbox = driver.find_element(By.ID, "exampleCheck1")

# click on checkbox
checkbox.click()

# validate if the checkbox is selected
assert checkbox.is_selected()

# locate the email textbox
# regular css_selector syntax:  tagname[attribute_name = 'value'] # tagname is optional here
driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys("abcd@gmail.com")

# locate the password textbox
# regular syntax: //tagname[@attribute_name = 'value']
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("12345")

# locate the submit button
# css
# driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
# xpath
# driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

# locate the submit button with css_selector using regular expression syntax
# css- reg expr syntax: tagname[attribute_name*='value']
# driver.find_element(By.CSS_SELECTOR, "input[class*= 'success']").click()

# xpath- reg expr syntax: //tagname[contains(@attribute, 'value')]
driver.find_element(By.XPATH, "//input[contains(@class,'success')]").click()

# fetch the success message after clicking submit btn
# class_name
success_msg = driver.find_element(By.CLASS_NAME, "alert-success").text[2:]
print(success_msg)
## print("Hello my name is Syed")
####### assert is a good command to remember
# print("none")
# print("hello")
# print("bye")
# print("syed push")
# print("ips push")
time.sleep(3)
driver.close()


# print("syed amazing push")

