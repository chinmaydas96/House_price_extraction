from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time



option = webdriver.ChromeOptions()
#option.add_argument(" — incognito")


browser = webdriver.Chrome(executable_path='/home/bat/my_project/webScraping/chromedriver', chrome_options=option)

a = browser.get("https://www.zillow.com/homes/for_sale/7018446_zpid/globalrelevanceex_sort/36.231968,-115.096504,36.231016,-115.100168_rect/17_zm/")

time.sleep(5)


element = []
try:
	print(element.append(browser.find_element_by_xpath("/html/body/div/")))
	
	browser.quit()
	
except :
	
	browser.quit()



