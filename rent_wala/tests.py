# from django.test import TestCase
# # import geocoder
# # import socket
# # from Crypto.PublicKey import RSA
# #
# # key = RSA.generate(1024)
# # encrypted_key = key.export_key()
# # encrypted_key = str(encrypted_key)
# # encrypted_key = encrypted_key[50:150]
# # print(encrypted_key)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from lxml import html
import time
import random


#def clck(xpth):

while True:
    driver = webdriver.Chrome("C:/Users/Abhishek/AppData/Local/Temp/Rar$EX00.390/chromedriver.exe")
    driver.get("https://www.sxpon.com")
    p = driver.current_window_handle
    for i in range(0, 30):
        #element = driver.fin
        driver.find_element_by_link_text('SXPON').click()
        chwd = driver.window_handles
        driver.switch_to.window(p)
        time.sleep(random.randint(2, 10))
        print("clicked")
    time.sleep(60)
    #password
    # element2 = driver.find_element_by_xpath('your xpath')
    # element2.send_keys("yourpass")

    #submit

#clck('/html/body/a[1]')
