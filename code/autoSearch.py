from selenium import webdriver
import time
import pyautogui as pag
import datetime
from retry import retry
import logging

class Autosearch(object):
    logging.basicConfig()
    # @retry(tries=10, delay=1,jitter=1)
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def my_input(self):
        # self.name:
        self.name = input("Name of item: ")
        self.max_price = input("The highest price you excpet for this item: ")
        self.min_price = input("The lowest price you excpet for this item(if not hit enter): ")
        if not self.min_price.isdigit():
            self.min_price = 0
        self.url = input ("Which website you looking for(if not hit enter): ")
        if self.url == "":
            self.url = 'https://www.amazon.com'

    def buy(self):
        self.driver.find_element_by_xpath('//*[@id="J_juValid"]/div[1]/a').click()
        pag.scroll(-900)
        self.driver.find_element_by_class_name('go-btn').click()
    
    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def search(self):
        search_name = self.name.replace(" ", "+")
        self.driver.get(self.url +"/s?k="+ search_name +"&ref=nb_sb_noss_1")

    def test(self):
        self.my_input()
        self.search()
        return Ture;
        #self.driver.close()

