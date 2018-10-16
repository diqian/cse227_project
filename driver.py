from selenium import webdriver
import time
# import urllib
# import urllib2

# x=raw_input("Enter the URL")
x = 'https://www.google.com/?gws_rd=ssl'
# refreshrate=raw_input("Enter the number of seconds")
refreshrate = int(5);
# refreshrate=int(refreshrate)
driver = webdriver.Firefox()
driver.get(x)
while True:
  time.sleep(refreshrate)
  driver.refresh()