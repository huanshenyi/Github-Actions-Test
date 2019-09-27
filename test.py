from selenium import webdriver
import time
import os
import sys

#process.env.PATH = f"{process.env.PATH};{os.getcwd()}/Selenium.WebDriver.IEDriver.3.150.0/driver"
#path =  "D:\a\Github-Actions-Test\Github-Actions-Test\Selenium.WebDriver.IEDriver.3.150.0\driver"

driver = webdriver.Ie(executable_path="Selenium.WebDriver.IEDriver.3.150.0\driver\IEDriverServer.exe")
driver.get('https://bell-face.co/')
# con_btn = driver.find_element_by_partial_link_text('（資料ダウンロード）')
# con_btn.click()
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()

