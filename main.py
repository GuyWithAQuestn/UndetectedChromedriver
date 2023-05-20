
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import io
import os

def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower():
                return True
    except Exception:
        pass
        return False


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Detect if we're running on a Pi or something else
if (is_raspberrypi()):
    print("returned True. This is a Pi")
    # use the existing chromedriver instead of downloading
    driver = uc.Chrome(driver_executable_path="/home/pi/.local/share/undetected_chromedriver/chromedriver_copy")
else:
    print("retruned False. This is not a Pi.")
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