from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://hoopshype.com/salaries/players/'

browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')
browser.get(url)

