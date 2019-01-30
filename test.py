import pyautogui
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
  
  ###### vao trang mua ban ########
  link_muaban = driver.find_element_by_xpath(".//a[contains(@href,'btc/vn')]")
  time.sleep(5)

  #elems.reverse()

  #for i in range(0, 5):
  #  print(elems[i].get_attribute('innerHTML'))
  
  #time.sleep(2)

#for element in elems:
#    print(element.get_attribute('innerHTML'))
#driver.quit()

#print("go")

#print(pyautogui.size())

#driver = webdriver.PhantomJS(executable_path='C:/Users/Anh Khoa/Documents/python_3.5_project/test Mouse and Keyboard and inspect web/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe') # or add to your PATH
#driver.set_window_size(1024, 768) # optional
#driver.get('https://remitano.com/btc/vn')
#driver.open('https://remitano.com/btc/vn')

#html = driver.execute_script("return document.getElementById('remitano-react-app').innerHTML")
#print(html)

#print(driver.page_source)

#res = requests.get('https://remitano.com/btc/vn')
#soup = bs4.BeautifulSoup(res.text,'html.parser')

#print(res.text)
#print(soup)



#html = urllib.request.urlopen("https://remitano.com/btc/vn").read()

#soup = BS(html)

#print soup.findAll(tag_name).get_text()

#print(html)

#width, height = pyautogui.size()

#for i in range(2):
#  pyautogui.moveTo(100, 100, duration=0.25)
#  pyautogui.moveTo(200, 100, duration=0.25)
#  pyautogui.moveTo(200, 200, duration=0.25)
#  pyautogui.moveTo(100, 200, duration=0.25)
  
#pyautogui.click(100, 150, button='left')

