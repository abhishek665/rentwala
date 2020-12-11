# # print(encrypted_key)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from lxml import html
import time
import random


#def clck(xpth):



while True:
    driver = webdriver.Chrome("C:/Users/Abhishek/AppData/Local/Temp/Rar$EX00.937/chromedriver.exe")

    for i in range(0, 30):
        #element = driver.fin
        driver.get("https://www.sxpon.com")
        driver.find_element_by_link_text('SXPON').click()
        time.sleep(random.randint(0, 20))
        print("clicked")
    time.sleep(60)