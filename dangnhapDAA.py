import pyautogui
import urllib.request
import requests, bs4
#from bs4 import BeautifulSoup as BS

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.action_chains import ActionChains
import time

service = service.Service('C:/Users/Anh Khoa/Documents/python_3.5_project/test Mouse and Keyboard and inspect web/chromedriver_win32/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('https://daa.uit.edu.vn/');
time.sleep(2) # Let the user actually see something!
elem = driver.find_element_by_id("edit-name")
pass_elem = driver.find_element_by_id("edit-pass")
login_elem = driver.find_element_by_id("edit-submit--2")

time.sleep(2)
actions = ActionChains(driver)
driver.find_element_by_xpath("//select[@class='links']/option[text()='-- Website trường']").click()

print(elem.get_attribute('innerHTML'))
#ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
actions.move_to_element(elem)
actions.send_keys_to_element(elem, '15520364')
  
actions.move_to_element(pass_elem)
#actions.send_keys_to_element(pass_elem, '*****')

#actions.click(login_elem)

#actions.perform()

actions.reset_actions()

time.sleep(3) # Let the user actually see something!

driver.get('https://daa.uit.edu.vn/');
actions = ActionChains(driver)
#print(driver.page_source)




#user = driver.find_element_by_xpath(".//a[contains(@href,'/user')]")
#kqhoctap = driver.find_element_by_xpath(".//a[contains(@href,'sinhvien/kqhoctap')]")

print(kqhoctap.get_attribute('innerHTML'))
#actions.click(user)
#actions.click(kqhoctap)
#actions.perform()

#driver.get('https://daa.uit.edu.vn/sinhvien/kqhoctap');

time.sleep(5) # Let the user actually see something!
#driver.quit()