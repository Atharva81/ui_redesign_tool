from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import webbrowser
import time

new=1
# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path='/home/ayush/Desktop/chromedriver', chrome_options=option)

# go to website of interest
browser.get("https://www.ndtv.com/latest?pfrom=home-topnavigation")

# wait up to 10 seconds for page to load
timeout = 2
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='nstory_header']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


# get all of the titles for the financial values
titles_element = browser.find_elements_by_xpath("//div[@class='nstory_header']")
titles = [x.text for x in titles_element]
'''
WRITTEN AS A NORMAL FOR LOOP:
titles = []
for x in titles_element:
    titles.append(x.text)
'''


# get all of the financial values themselves
values_element = browser.find_elements_by_xpath("//div[@class='nstory_intro']")
values = [x.text for x in values_element]  # same concept as for-loop/list-comprehension above

f=open("temp.html","w")
for t,v in zip(titles, values):
    f.write("<h3 style=\"color:red\"> "+t+"</h3> <p style=\"color: blue\">"+v+"</p><br>")
'''
chrome_path='/usr/bin/google-chrome %s'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
driver=webbrowser.get(using='google-chrome').open("temp.html")
time.sleep(3)
'''
webbrowser.open("temp.html", new=new)