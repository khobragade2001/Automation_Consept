import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
x = By.XPATH
d.implicitly_wait(10)
d.get("https://the-internet.herokuapp.com/upload")
d.find_element(x, "//input[@id='file-upload']").send_keys("C:\\Automation\\screenshotss\\img.jpg")
d.find_element(x, "//input[@id='file-submit']").click()
time.sleep(2)
d.save_screenshot("C:\\Automation\\screenshots\\imnhg0.jpg")
