from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome("./chromedriver")
actions = ActionChains(driver)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//div[@class='nav-search-scope nav-sprite']").click()
driver.find_element_by_xpath("//option[text()='Baby']").click()
a = driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
sleep(4)
actions.send_keys(Keys.PAGE_DOWN).perform()
sleep(5)
driver.find_element_by_xpath("//img[@alt='Cable World® Musical Keyboard Mat Piano Gym Mat Gym & Fitness ']/../../..//span[text()='Cable World® Musical Keyboard Mat Piano G…']").click()
ope1 = driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
actions.move_to_element(ope1).perform()
ope2 = driver.find_element_by_xpath("Create a Wish List")
actions.move_to_element(ope2).perform()
ope2.click()