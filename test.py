from selenium import webdriver
import time
import os
import sys

path =  f"{sys.argv[0]}/Selenium.WebDriver.IEDriver.3.150.0/driver"
print(path)


driver = webdriver.Ie(executable_path=path)
driver.get('https://bell-face.co/')
con_btn = driver.find_element_by_partial_link_text('（資料ダウンロード）')
con_btn.click()
time.sleep(2)
driver.close()
driver.quit()

