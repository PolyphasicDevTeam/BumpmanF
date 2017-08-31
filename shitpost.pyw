import time
import wget
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pause

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\StarmanF\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 5\\")
w = webdriver.Chrome(executable_path="C:\\ChromeWebdriver\\chromedriver.exe", chrome_options=options)

w.get("https://discordapp.com/channels/249219704655183876/257401368807997440")
time.sleep(5)

while 1:
	elem = w.find_element_by_xpath("//div[@class='']//*[@placeholder='Message #botspam_shitpost']")
	elem.send_keys("=bump")
	elem.send_keys(Keys.RETURN)
	elem.send_keys(".pick")
	elem.send_keys(Keys.RETURN)
	pause.hours(4.02)