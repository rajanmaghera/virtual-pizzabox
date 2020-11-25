from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("user-data-dir=/Users/rajanmaghera/Library/Application Support/Google/Chrome/")
driver = webdriver.Chrome(options=options)
driver.get("https://jamboard.google.com/d/1VlPI95UDlq2KhqMGtL6f9ftgsLPN0Zzch2hsOh91lVo")

import time

time.sleep(5)

shape_button = driver.find_element(By.ID, "shapeButton")
webdriver.ActionChains(driver).click(shape_button).perform()

driver.find_element(By.CLASS_NAME, "jam-drawing-element-canvas")


