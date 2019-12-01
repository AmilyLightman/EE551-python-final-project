from selenium import webdriver
import time
import logging
import datetime

class AutoBuy(object):
    logging.basicConfig()

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.name = "CARIEDO"
        self.url = 'https://s.taobao.com'
        self.buytime = "2019-11-30 11:00:00"

    def my_input(self):
        # self.name:
        self.name = input("Name of item: ")
        #self.max_price = input("The highest price you excpet for this item: ")
        #self.min_price = input("The lowest price you excpet for this item(if not hit enter): ")
        #if not self.min_price.isdigit():
        #    self.min_price = 0
        self.url = input("Which website you looking for(if not hit enter): ")
        if self.url == "":
            self.url = 'https://s.taobao.com'
        self.buytime = input("Which time you wanna buy it(year-mon-day hour:min:sec): ")
        if self.buytime == "":
            self.buytime = "2019-11-30 11:00:00"

    def buy(self):
        try:
            if self.driver.find_element_by_id("J_SelectAll1"):
                self.driver.find_element_by_id("J_SelectAll1").click()
                print("select all")
            try:
                if self.driver.find_element_by_id("J_Go"):
                    self.driver.find_element_by_id("J_Go").click()
                    print("submit the order")
                self.driver.find_element_by_link_text('提交订单').click()
                print("place the order")
            except:
                time.sleep(3)
        except:
            time.sleep(3)


    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
        time.sleep(10)
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


    def search(self):
        search_name = self.name.replace(" ", "+")
        self.driver.get(self.url + "/search?q=" + search_name + "&js=1&initiative_id=staobaoz_20191130&ie=utf8")

    def monitor(self):
        time.sleep(30)
        self.driver.get("https://cart.taobao.com/cart.htm")
        interval = 0.1
        last = 1800
        elapse = 0
        while elapse < last:
            t = datetime.datetime.now()
            now = t.strftime('%Y-%m-%d %H:%M:%S')
            print('The time now is %s' % (now))
            if now >= self.buytime:
                print("going to buy it")
                self.buy()
                return
            else:
                print("not the time yet")
            time.sleep(interval)
            elapse += interval

    def run(self):
        try:
            self.login()
            self.search()
            self.monitor()
            self.driver.close()
            return True
        except:
            return False

if __name__ == "__main__":
    my_buy = AutoBuy()
    my_buy.run()