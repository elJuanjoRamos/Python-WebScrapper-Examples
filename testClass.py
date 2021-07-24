from io import SEEK_CUR
import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class PayInPython(unittest.TestCase):
    def __init__(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('http://www.python.org')

    def click_pay(self):
        element = self.browser.find_element_by_class_name("donate-button")
        element.click()

    def set_donation(self):
        checker = self.browser.find_element_by_id('CIVICRM_QFID_19_4')
        checker.click()

    def set_contribute(self):
        recibe = self.browser.find_element_by_id('is_recur')
        recibe.click()

    def set_select(self):
        select = Select(self.browser.find_element_by_name('frequency_unit'))
        select.select_by_index(1)



clase = PayInPython()

clase.click_pay()
clase.set_donation()
clase.set_contribute()
clase.set_select()

