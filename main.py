from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.python.org'

browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')
browser.get(url)

assert "Python" in browser.title

elemnt = browser.find_element_by_name("q")
elemnt.clear()
elemnt.send_keys("pycon")
elemnt.send_keys(Keys.RETURN)

assert "No results found." not in browser.page_source

# browser.close()
