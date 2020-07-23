import time
from selenium import webdriver


browser = webdriver.Chrome()  # Chrome

url = "https://google.com"
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
<textarea name='??'></textarea>


<input name="q" type="text">
"""
"""
<input type='submit' />
<button type='submit' />
<form></form>

<input value="Google Search" aria-label="Google Search" name="btnK" type="submit">
"""

time.sleep(2)  # slow the process of searching for the element
name = "q"
search_el = browser.find_element_by_name(
    name
)  # find the input field on the google search page
search_el.send_keys("Selenium Python")  # input text in the field
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el)
time.sleep(2)
submit_btn_el.click()
