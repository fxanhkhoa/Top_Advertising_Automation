import urllib.request
import requests, bs4
#from bs4 import BeautifulSoup as BS

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import time

proxy = Proxy(
     {
          'proxyType': ProxyType.MANUAL,
          'httpProxy': 'ip_or_host:port'
     }
)

service = service.Service('C:/Users/Anh Khoa/Documents/python_3.5_project/test Mouse and Keyboard and inspect web/chromedriver_win32/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)

input("Press Enter to continue...")

while True:
  driver.get('https://remitano.com/btc/vn');
  time.sleep(5) # Let the user actually see something!
  #print(driver.page_source)
  #elems = driver.find_elements_by_class_name("amount")

  #elems.reverse()
  
  #for i in range(0, 5):
  #  print(elems[i].get_attribute('innerHTML'))
  
  #time.sleep(2)
  
  ######### Part Calculate Price #########
  
  ######### Part Post Advertisement After login using link #########
  
  ## go to offer page
  driver.get('https://remitano.com/btc/vn/offers/create');
  actions = ActionChains(driver)
  
  ## find thay doi class
  elems_change = driver.find_elements_by_class_name("btn_change")
  for i in range(0,1):
    print(elems_change[i]/get_attribute('innerHTML'))
  
  ## ==> click
  actions.click(elems_change[0])
  
  ## find price field
  elem_price = driver.find_element_by_name('price').send_keys("******")
  
  ## find bank name field and click
  driver.find_element_by_xpath("//select[@name='payment_details.bank_name']/option[text()='ACB (Ngân hàng Á Châu)']").click()
  
  ## find account number and click
  driver.find_element_by_name('payment_details.bank_account_number').send_keys("*********")
  
  ## find account name
  driver.find_element_by_name('payment_details.bank_account_name').send_keys("*********")
  
  ## click create btn
  #driver.find_elements_by_class_name("btn-save-offer").click()
  
#for element in elems:
#    print(element.get_attribute('innerHTML'))
#driver.quit()

