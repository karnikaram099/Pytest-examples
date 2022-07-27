from selenium import webdriver
import pytest
from pytest import fixture
button_login_Xpath = "(//span[text()='Jobseeker Login'])[3]"
textbox_email_id = "signInName"
textbox_password_id = "password"
@fixture
def _driver():
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://www.monsterindia.com/")
    return driver
def test_login(_driver):
    _driver.find_element_by_xpath(button_login_Xpath).click()
    _driver.find_element_by_id(textbox_email_id).send_keys("karnikaram.2000@gmail.com")
    _driver.find_element_by_id(textbox_password_id).send_keys("172N1A0317@r")
    _driver.close()

    
# from pytest import fixture
# @fixture
# def greet():
#     return "Hello world"
# def test_greet(greet):
#     assert "Hello world"==greet




