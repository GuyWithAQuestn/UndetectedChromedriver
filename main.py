
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from bs4 import BeautifulSoup


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = uc.Chrome()

driver.get("https://www.nowsecure.nl")
# search = driver.find_element(by=By.NAME,value="q")
# search.send_keys("Selenium")
# search.send_keys(Keys.ENTER)


# # Get the page content
page_content = driver.page_source
page_content_soup = BeautifulSoup(page_content, 'lxml')

print("page_content_soup")
print(page_content_soup)