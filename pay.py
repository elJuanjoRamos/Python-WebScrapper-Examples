from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'http://www.python.org'

browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')
browser.get(url)


element = browser.find_element_by_class_name("donate-button")

if browser.find_element_by_class_name("donate-button"):
    print('existe el elemento')
else:
    print('no existe el elemento')
    

element.click()



checker = browser.find_element_by_id('CIVICRM_QFID_19_4')
checker.click()


recibe = browser.find_element_by_id('is_recur')
recibe.click()

select = Select(browser.find_element_by_name('frequency_unit'))
select.select_by_index(1)

input1 = browser.find_element_by_id('installments')
input1.send_keys('hola')