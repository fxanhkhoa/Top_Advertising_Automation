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

DELAY_FOR_EACH_PAGE = 2.5
MAXIMUM_BTC = 1
NUMBER_OF_PAGE_WANT_TO_CHECK = 10

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
  try:
    driver.get('https://remitano.com/btc/vn/offers/create');
    time.sleep(5) # Let the user actually see something!
    actions = ActionChains(driver)
    elems_change = driver.find_elements_by_class_name("btn-change")
    for i in range(0,1):
      print(elems_change[i].get_attribute('innerHTML'))
      
    ## ==> click
    actions.click(elems_change[0])
    actions.perform()
    time.sleep(3)
    # driver.get('https://remitano.com/btc/vn');
    # time.sleep(5) # Let the user actually see something!
    # #print(driver.page_source)
    
    # ########### Get 10 page on advertising prices #########
    # price = []
    # limit_BTC = []
    
    # ######### Part Get minimum price #########
    
    # for time_count in range(0, NUMBER_OF_PAGE_WANT_TO_CHECK):
      # elems = driver.find_elements_by_class_name("amount")
      # elems_tradelimit = driver.find_elements_by_class_name("remi-offer-item-price-trade-limits")
      # elems.reverse()
      # elems_tradelimit.reverse()
      
      # for i in range(0, 5):
        # value = float(elems[i].get_attribute('innerHTML').replace(",", ""))
        # print(float(value))
        # max_value_str = elems_tradelimit[i].text.replace("Tối đa: ", "")
        # max_value = float(max_value_str.replace(" BTC", ""))
        # #print(int(elems[i].get_attribute('innerHTML')) * 2)
        # print(max_value)
        
        # if (max_value >= MAXIMUM_BTC):
          # price.append(value)
          # limit_BTC.append(max_value)
      
      # value = "Trang sau"
      # requiredXpath = "//a[text()=\'"+value+"\']"
      # driver.find_element_by_xpath(requiredXpath).click()
        
      # #print(elem.get_attribute('innerHTML'))
      
      # time.sleep(DELAY_FOR_EACH_PAGE)
    
    # #### Let's sort and find the lowest price with BTC > 1 ####
    # print('Minimum price: ',min(price))
    # time.sleep(1)
    
    # ######### Part Calculate Price #########
    
    # ## go to offer page
    # driver.get('https://remitano.com/btc/vn/offers/create');
    # actions = ActionChains(driver)
    
    # ## Get Bitstamp BTC
    # BTC_stamp = float(driver.find_elements_by_class_name("text-primary"))
    # print(BTC_stamp)
    
    # ## Calculate
    # bitUSD = min(price) / BTC_stamp
    # bitUSD_deserve = bitUSD + 12
    
    # can_post = 0
    
    # if ((bitUSD_deserve * BTC_stamp) - min(price) >= 50):
      # can_post = 1
    
    ######### Part Post Advertisement After login using link #########
    
    # ## find thay doi class
    # elems_change = driver.find_elements_by_class_name("btn_change")
    # for i in range(0,1):
      # print(elems_change[i]/get_attribute('innerHTML'))
    
    # ## ==> click
    # actions.click(elems_change[0])
    
    # ## find price field
    # elem_price = driver.find_element_by_name('price').send_keys("******")
    
    # ## find bank name field and click
    # driver.find_element_by_xpath("//select[@name='payment_details.bank_name']/option[text()='ACB (Ngân hàng Á Châu)']").click()
    
    # ## find account number and click
    # driver.find_element_by_name('payment_details.bank_account_number').send_keys("*********")
    
    # ## find account name
    # driver.find_element_by_name('payment_details.bank_account_name').send_keys("*********")
    
    ## click create btn
    #if can_post == 1:
      #driver.find_elements_by_class_name("btn-save-offer").click()
      
  except Exception as e:
    print(e)
#for element in elems:
#    print(element.get_attribute('innerHTML'))
#driver.quit()

