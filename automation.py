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
ACCOUNT_NUMBER = lines[5][lines[5].index('=') + 1 : lines[5].index('=') + len(lines[5]) - lines[5].index('=')]
ACCOUNT_NAME = lines[6][lines[6].index('=') + 1 : lines[6].index('=') + len(lines[6]) - lines[6].index('=')]
minus_price = int(lines[7][lines[7].index('=') + 1 : lines[7].index('=') + len(lines[7]) - lines[7].index('=')])
BIT_TO_SELL = float(lines[8][lines[8].index('=') + 1 : lines[8].index('=') + len(lines[8]) - lines[8].index('=')])
BANK_NAME = lines[9][lines[9].index('=') + 1 : lines[9].index('=') + len(lines[9]) - lines[9].index('=')]

print(DELAY_FOR_EACH_PAGE, MAXIMUM_BTC, NUMBER_OF_PAGE_WANT_TO_CHECK, DELAY_FOR_EACH_TIME_POST, LINK_FOR_TOKEN_LOG_IN, ACCOUNT_NUMBER, ACCOUNT_NAME, BANK_NAME, minus_price)

proxy = Proxy(
     {
          'proxyType': ProxyType.MANUAL,
          'httpProxy': 'ip_or_host:port'
     }
)

service = service.Service(os.getcwd()+ '/chromedriver_win32/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)

driver.get(LINK_FOR_TOKEN_LOG_IN)

input("Wait for Website done loading and Create one Advertisement and Press Enter to continue...")

step1 = 0
step2 = 0

while True:
  try:
    driver.get('https://remitano.com/btc/vn')
    time.sleep(5) # Let the user actually see something!
    print(driver.page_source)
    ##### try click vietnam #####
    try:
      requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]"
      #driver.find_element_by_xpath(requiredXpath)
      driver.find_element_by_xpath(requiredXpath).click()
      time.sleep(1)
      
      value = "Việt Nam"
      requiredXpath = "//span[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
      time.sleep(3)
      
    except Exception as e:
      print(e)
    
    #print(driver.page_source)
    
    ########### Get 10 page on advertising prices #########
    price = []
    limit_BTC = []
    
    ######### Part Get minimum price #########
    
    for time_count in range(2, NUMBER_OF_PAGE_WANT_TO_CHECK):
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
    
    print("out here")
    #### Let's sort and find the lowest price with BTC > MAXIMUM_BTC ####
    print('Minimum price: ',min(price))
    time.sleep(1)
    
    ######### Part Delete Post #########
    
    try:
      ## Go to Control board
      driver.get('https://remitano.com/btc/vn/dashboard/escrow/trades/active');
      time.sleep(1)
      
      try:
        requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]"
        #driver.find_element_by_xpath(requiredXpath)
        driver.find_element_by_xpath(requiredXpath).click()
        time.sleep(1)
        
        value = "Việt Nam"
        requiredXpath = "//span[text()=\'"+value+"\']"
        driver.find_element_by_xpath(requiredXpath).click()
        time.sleep(3)
      
      except Exception as e:
        print(e)
      
      ## Go to my advertising board
      value = "Các quảng cáo của tôi"
      requiredXpath = "//span[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
      
      time.sleep(2)
      
      ## Delete advertisement
      value = "Xóa"
      requiredXpath = "//span[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
      
      time.sleep(2)
      
      ## Accept button
      value = "Đồng ý"
      requiredXpath = "//button[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
      
      time.sleep(5)
    except Exception as e:
      print('no ad to delete')
      print(e)
    
    ######### Part Calculate Price #########
    
    ## go to offer page
    driver.get('https://remitano.com/btc/vn/offers/create')
    time.sleep(1)
    
    try:
      requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]"
      #driver.find_element_by_xpath(requiredXpath)
      driver.find_element_by_xpath(requiredXpath).click()
      time.sleep(1)
      
      value = "Việt Nam"
      requiredXpath = "//span[text()=\'"+value+"\']"
      driver.find_element_by_xpath(requiredXpath).click()
      time.sleep(3)
      
    except Exception as e:
      print(e)
    #actions = ActionChains(driver)
    
    ## Get Bitstamp BTC
    BTC_stamp_str = driver.find_elements_by_class_name("text-primary")
    BTC_stamp = float(BTC_stamp_str[0].get_attribute('innerHTML'))
    print(BTC_stamp)
    
    ## Calculate
    bitUSD = min(price) / BTC_stamp
    bitUSD_deserve = bitUSD*0.995
    
    can_post = 0
    print('price after: ', bitUSD_deserve * BTC_stamp)
    
    if ((bitUSD_deserve * BTC_stamp) - min(price) <= 30000):
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
	
    if (BIT_TO_SELL > 0):
    ## find detail label
      try:
        requiredXpath = "//label[contains(text(),'Chi tiết')]"
        driver.find_element_by_xpath(requiredXpath).click()
        time.sleep(3)
      except Exception as e:
        print(e)
      
    ## find btc max
      elems_change = driver.find_elements_by_class_name("btn-change")
    
      #actions.click(elems_change[2])
      #actions.perform()
      elems_change[4].click()
    
      time.sleep(2)
      driver.find_element_by_name('max_amount').clear()
      elem_price = driver.find_element_by_name('max_amount').send_keys(str(BIT_TO_SELL))
    
    ## find price field
    driver.find_element_by_name('price').clear()
    elem_price = driver.find_element_by_name('price').send_keys(str(bitUSD_deserve))
    
    ## find bank name field and click
    driver.find_element_by_xpath("//select[@name='payment_details.bank_name']/option[text()='"+ BANK_NAME +"']").click()
    
    ## find account number and click
    driver.find_element_by_name('payment_details.bank_account_number').send_keys(ACCOUNT_NUMBER)
    
    ## find account name
    driver.find_element_by_name('payment_details.bank_account_name').send_keys(ACCOUNT_NAME)
    time.sleep(3)
    
	
    ## click create btn
    if can_post == 1:
      time.sleep(1)
      value = "Tạo"
      #requiredXpath = "//button[text()=\'"+value+"\']"
      requiredXpath = "//button[contains(@class, 'btn-save-offer btn btn-primary')]"
      click_ok = 0
      try:
        driver.find_element_by_xpath(requiredXpath).click()
        click_ok = 1
      except Exception as e:
        print(e)
		
      try:
        if click_ok == 0:
          driver.find_element_by_xpath(requiredXpath)
      except Exception as e:
        print(e)
      
      print('clicked')
      time.sleep(10)
      
      try:
        value = "Đồng ý"
        requiredXpath = "//button[text()=\'"+value+"\']"
        driver.find_element_by_xpath(requiredXpath).click()
        print("accept clicked")
        time.sleep(2)
      except Exception as e:
        print(e)
    
    ## done 1 time
    ## time.sleep(DELAY_FOR_EACH_TIME_POST)
 
  except Exception as e:
    print(e)

  try:
        driver.get('https://remitano.com/btc/vn')

        ###### Get Language Viet Nam ######
        try:
            requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]"
            #driver.find_element_by_xpath(requiredXpath)
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(1)
            
            value = "Việt Nam"
            requiredXpath = "//span[text()=\'"+value+"\']"
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(3)
            
        except Exception as e:
            print(e)

        ######### Click Ban Ngay ########
        try:
            requiredXpath = "//div[contains(@class, 'quick-tab buy-offer-list')]"
            #driver.find_element_by_xpath(requiredXpath)
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(1)
            
        except Exception as e:
            print(e)

        ######### Get price #########
        price = []

        for time_count in range(1, 2):
            elems = driver.find_elements_by_class_name("amount")
            elems.reverse()

            for i in range(0, 3):
                value = float(elems[i].get_attribute('innerHTML').replace(",", ""))
                print(float(value))
                price.append(value)

            value = "Trang sau"
            requiredXpath = "//a[text()=\'"+value+"\']"
            driver.find_element_by_xpath(requiredXpath).click()

            time.sleep(DELAY_FOR_EACH_PAGE)
        
        print("Maximum price: ", max(price))

        ######### Delete Buy Post #########

        ######### Post Buy Post #########
        driver.get('https://remitano.com/btc/vn/offers/create')
        time.sleep(1)

        ###### Get Language Viet Nam ######
        try:
            requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]"
            #driver.find_element_by_xpath(requiredXpath)
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(1)
            
            value = "Việt Nam"
            requiredXpath = "//span[text()=\'"+value+"\']"
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(3)
            
        except Exception as e:
            print(e)

        ######### Click Mua BTC ########
        try:
            requiredXpath = "//label[contains(@class, 'offer-type-buy btn btn-default')]"
            #driver.find_element_by_xpath(requiredXpath)
            driver.find_element_by_xpath(requiredXpath).click()
            time.sleep(1)
            
        except Exception as e:
            print(e)

        ######### Calculate #########

        BTC_stamp_str = driver.find_elements_by_class_name("text-primary")
        BTC_stamp = float(BTC_stamp_str[0].get_attribute('innerHTML'))
        print(BTC_stamp)
        
        ## Calculate
        bitUSD = max(price) / BTC_stamp
        bitUSD_deserve = bitUSD*1.01

        print('price after: ', bitUSD_deserve * BTC_stamp)

        elems_change = driver.find_elements_by_class_name("btn-change")
        elems_change[0].click()

        ## find price field
        driver.find_element_by_name('price').clear()
        elem_price = driver.find_element_by_name('price').send_keys(str(bitUSD_deserve))

        ## find bank name field and click
        driver.find_element_by_xpath("//select[@name='payment_details.bank_name']/option[text()='"+ BANK_NAME +"']").click()

        time.sleep(1)
        value = "Tạo"
        #requiredXpath = "//button[text()=\'"+value+"\']"
        requiredXpath = "//button[contains(@class, 'btn-save-offer btn btn-primary')]"
        click_ok = 0
        
        try:
            driver.find_element_by_xpath(requiredXpath).click()
            click_ok = 1
        except Exception as e:
            print(e)
            
        try:
            if click_ok == 0:
                driver.find_element_by_xpath(requiredXpath)
        except Exception as e:
            print(e)
        
        print('clicked')
        time.sleep(4)

        try:
            value = "Đồng ý"
            requiredXpath = "//button[text()=\'"+value+"\']"
            driver.find_element_by_xpath(requiredXpath).click()
            print("accept clicked")
            time.sleep(2)
        except Exception as e:
            print(e)

        time.sleep(DELAY_FOR_EACH_TIME_POST)
  except Exception as e:
      print(e)
