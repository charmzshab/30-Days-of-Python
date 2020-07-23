# import getpass

# my_password = getpass.getpass("What is ny password?\n")

# print(my_password)
import time
from conf import INSTA_PASSWORD, INSTA_USERNAME
from selenium import webdriver

browser = webdriver.Chrome()
time.sleep(40)
url = "https://www.instagram.com"
browser.get(url)

username_el = browser.find_element_by_name("username")
username_el.sendkeys(INSTA_USERNAME)

password_el = browser.find_element_by_name("password")
password_el.sendkeys(INSTA_PASSWORD)

time.sleep(2)

submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

"""
<input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value="">

<input aria-label="Password" aria-required="true" autocapitalize="off" autocorrect="off" name="password" type="password" class="_2hvTZ pexuQ zyHYP" value="">

<button type="submit">
"""
