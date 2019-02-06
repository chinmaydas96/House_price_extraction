from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time



option = webdriver.ChromeOptions()
option.add_argument(" — incognito")



import csv

with open('stock.csv', mode='w') as stock:
    stock_writer = csv.writer(stock, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    # Set the name of the columns

    stock_writer.writerow(['V1','V2','V3','V4','V5'])

while(True):

	browser = webdriver.Chrome(executable_path='/home/bat/webScraping/chromedriver', chrome_options=option)
	
	a = browser.get("https://www.tradingview.com/chart/yX7UiaCU/?symbol=BINANCE:fuelBTC&interval=60")
	
	time.sleep(5)

	
	element = []
	try:
		element.append(browser.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[3]/td[2]/div/div/div/div/span[6]").text)
		element.append(browser.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[5]/td[2]/div/div/div/div/span[1]").text)
		element.append(browser.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[5]/td[2]/div/div/div/div/span[2]").text)
		element.append(browser.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[7]/td[2]/div/div/div/div/span[1]").text)
		element.append(browser.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[7]/td[2]/div/div/div/div/span[2]").text)

		print(element)
		
		browser.quit()


		with open('stock.csv', mode='a') as stock:
		    stock_writer = csv.writer(stock, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		    stock_writer.writerow(element)
		

		# Set the time sleep after which the data will be extracted

		time.sleep(20)
		
	except :
		
		browser.quit()



