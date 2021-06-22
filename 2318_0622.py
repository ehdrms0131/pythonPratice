pip install selenium #셀레니움을 설치해준다

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver = 'C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.python.org")
assert "Python" in driver.title
elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.naver.com")
assert "NAVER" in driver.title

elem=driver.find_element_by_name("query")
elem.clear()
elem.send_keys("BTS")
elem.send_keys(Keys.RETURN)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.daum.com")
assert "Daum" in driver.title

elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys("butter")
elem.send_keys(Keys.RETURN)
assert "No result found" not in driver.page_source

h2s = driver.find_elements_by_css_selector('#clusterResultUL > li > div.wrap_cont > div > div > a')
for h2 in h2s:
    print(h2.text)

driver.quit()