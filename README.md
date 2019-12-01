EE551-python-final-project
=====
**Automatic shopping**
_____
10440141 
Wanying Cao 
wcao9@stevens.edu

**Introduction**

With the development of the times, more and more people start shopping online. In a specific date, e-commerce will gives a huge discount.Such as the Black Friday in the USA and Nov 11 in China. It's hard to get what we want when so many people rush to purchase the same thing. Sometimes it will out of stock before I click the 'purchase' button. So, this project is making for automatically buy the products on Taobao website(which is a popular online shopping website in China).

**Prepare**   

using python version 3.0+
need to install selenium, chromedriver

ChromeDriver(for mac):  
mv chromedriver /usr/local/bin  
sudo chmod u+x,o+x   /usr/local/bin/chromedriver  

**Design**  

In order to automatically buy items on Taobao website, we need:
1. open the Taobao webpage
2. jump to its shopping cart 
3. submit the order
4. place the order

**Implement**

This is 7 functions in this project:

1.__init__ -- create a webdriver of Chrome using webdriver in selenium
2.input -- input information for the search item's name, the url of website(working for Taobao only now) and the time we want it to automatically buy
3.buy -- using for submit the order and place the order
4.login -- automatically open the login page for log in the accont
5.search -- search the name we inputed in input function(this is for future development)
6.monitor -- monitor the time for buy inputed in input function, only goes to buy function is the real time on the computer is equal or later than the time inputed. If the real time is early than the time we set, it will retry every 0.1 second, 30 minutes for total.
7.run -- this is the function how we run the taobao project

**Conclusion**

This project can automatically buy items in the shopping cart on Taobao website, And can search in Taobao website by name.
There is a video in folder video named taobao.mp4, recorded how a submitted one order in Taobao. if this is a discount start from 2019-11-30 12:00:00, we can run this project few minutes before 12 and set time for "2019-11-30 12:00:00". It will retry until the real time on the computer is 12, and it will automatically submit and place the order for us.

**Future development**

Search function is what I try to achieve for the futurn development, which can only search items by name now. I hope we could use image search(which Taobao has it, but Taobao can only use name or image for search, not both) to search the item, and siftings by price. That is also the reason I tried auto-search for Amazon, but Amazon's price tag is hard to find and modify frequently.

For input function, it is designed for using this auto-buy project for all websites. Unfortunately, every website has different tag for search. I used Beautiful Soup to analyze some websites, this is hard to achieve because most of them use different patten and name for tag. We might can do it base on machine learning. 
