import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
x = By.XPATH
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
dd = Select(driver.find_element(x, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))

dd.select_by_visible_text("India")
# dd.select_by_value("Iraq")###  error occure because of  Cannot locate option with value: Iraq;
dd.select_by_index(3)
driver.save_screenshot("C:\\Automation\\screenshots\\drop_down01.jpg")
time.sleep(2)


