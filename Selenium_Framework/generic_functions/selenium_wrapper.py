"""It will contain all the generic methods which are used to perform some actions"""
import locator as locator
from wait import demo
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver = driver
    def enter_text(self,locator,*, value):
        self.driver.find_element_by_xpath(*locator)
