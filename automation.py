import urllib.request
import requests, bs4
#from bs4 import BeautifulSoup as BS

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.action_chains import ActionChains
import time

import os
import sys

####### Read Config #########
fp = open(os.getcwd()+'\\Config.txt')
lines = fp.readlines()

DELAY_FOR_EACH_PAGE = float(lines[0][lines[0].index('=') + 1 : lines[0].index('=') + len(lines[0]) - lines[0].index('=')])
MAXIMUM_BTC = int(lines[1][lines[1].index('=') + 1 : lines[1].index('=') + len(lines[1]) - lines[1].index('=')])
NUMBER_OF_PAGE_WANT_TO_CHECK = int(lines[2][lines[2].index('=') + 1 : lines[2].index('=') + len(lines[2]) - lines[2].index('=')])
DELAY_FOR_EACH_TIME_POST = int(lines[3][lines[3].index('=') + 1 : lines[3].index('=') + len(lines[3]) - lines[3].index('=')])
LINK_FOR_TOKEN_LOG_IN = lines[4][lines[4].index('=') + 1 : lines[4].index('=') + len(lines[4]) - lines[4].index('=')]

print(DELAY_FOR_EACH_PAGE, MAXIMUM_BTC, NUMBER_OF_PAGE_WANT_TO_CHECK, DELAY_FOR_EACH_TIME_POST, LINK_FOR_TOKEN_LOG_IN)

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

driver.get(LINK_FOR_TOKEN_LOG_IN)

input("Wait for Website done loading and Create one Advertisement and Press Enter to continue...")

while True:
  try:
    driver.get('https://remitano.com/btc/vn');
    time.sleep(5) # Let the user actually see something!
    #print(driver.page_source)
    
    ########### Get 10 page on advertising prices #########
    price = []
    limit_BTC = []
    
    ######### Part Get minimum price #########
    
    for time_count in range(1, NUMBER_OF_PAGE_WANT_TO_CHECK):
      elems = driver.find_elements_by_class_name("amount")
      elems_tradelimit = driver.find_elements_by_class_name("remi-offer-item-price-trade-limits")
      elems.reverse()
      elems_tradelimit.reverse()
      
      for i in range(0, 5):
        value = float(elems[i].get_attribute('innerHTML').replace(",", ""))
        print(float(value))
        max_value_str = elems_tradelimit[i].text.replace("Tối đa: ", "")
        max_value = float(max_value_str.replace(" BTC", ""))
        #print(int(elems[i].get_attribute('innerHTML')) * 2)
        print(max_value)
        
        if (max_value >= MAXIMUM_BTC):
          price.append(value)
          limit_BTC.append(max_value)
      
      value = "Trang sau"
      requiredXpath = "//a[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
        
      #print(elem.get_attribute('innerHTML'))
      
      time.sleep(DELAY_FOR_EACH_PAGE)
    
    #### Let's sort and find the lowest price with BTC > MAXIMUM_BTC ####
    print('Minimum price: ',min(price))
    time.sleep(1)
    
    ######### Part Delete Post #########
    
    # ## Go to Control board
    # driver.get('https://remitano.com/btc/vn/dashboard/escrow/trades/active');
    # time.sleep(1)
    
    # ## Go to my advertising board
    # value = "Các quảng cáo của tôi"
    # requiredXpath = "//span[text()=\'"+value+"\']"
    # driver.find_element_by_xpath(requiredXpath).click()
    
    # ## Delete advertisement
    # value = "Xóa"
    # requiredXpath = "//span[text()=\'"+value+"\']"
    # driver.find_element_by_xpath(requiredXpath).click()
    
    # ## Accept button
    # value = "Đồng ý"
    # requiredXpath = "//button[text()=\'"+value+"\']"
    # driver.find_element_by_xpath(requiredXpath).click()
    
    # time.sleep(5)
    
    ######### Part Calculate Price #########
    
    ## go to offer page
    driver.get('https://remitano.com/btc/vn/offers/create');
    time.sleep(1)
    #actions = ActionChains(driver)
    
    ## Get Bitstamp BTC
    BTC_stamp_str = driver.find_elements_by_class_name("text-primary")
    BTC_stamp = float(BTC_stamp_str[0].get_attribute('innerHTML'))
    print(BTC_stamp)
    
    ## Calculate
    bitUSD = min(price) / BTC_stamp
    bitUSD_deserve = bitUSD - 12
    
    can_post = 0
    print('price after: ', bitUSD_deserve * BTC_stamp)
    
    if ((bitUSD_deserve * BTC_stamp) - min(price) >= 30000):
      can_post = 1
      print('can post = ', can_post)
    
    ######### Part Post Advertisement After login using link #########
    
    ## get action
    actions = ActionChains(driver)
    
    ## find thay doi class
    elems_change = driver.find_elements_by_class_name("btn-change")
    for i in range(0,1):
      print(elems_change[i].get_attribute('innerHTML'))
    
    ## ==> click
    actions.click(elems_change[0])
    actions.perform()
    time.sleep(2)
    
    ## find price field
    driver.find_element_by_name('price').clear()
    elem_price = driver.find_element_by_name('price').send_keys(str(bitUSD_deserve))
    
    ## find bank name field and click
    driver.find_element_by_xpath("//select[@name='payment_details.bank_name']/option[text()='Vietcombank']").click()
    
    ## find account number and click
    driver.find_element_by_name('payment_details.bank_account_number').send_keys("0071000720877")
    
    ## find account name
    driver.find_element_by_name('payment_details.bank_account_name').send_keys("Nguyen Hoai Son")
    
    ## click create btn
    #if can_post == 1:
      #driver.find_elements_by_class_name("btn-save-offer").click()
    
    ## done 1 time
    time.sleep(DELAY_FOR_EACH_TIME_POST)
 
  except Exception as e:
    print(e)
#for element in elems:
#    print(element.get_attribute('innerHTML'))
#driver.quit()




# href="/btc/vn/dashboard/escrow/trades/active" bang dieu khien

#Các quảng cáo của tôi
#Xóa
#Đồng ý
#btn btn-default
