
from pytest import fixture
from config import Config
@fixture               #passing some data like driver for all the test scripts
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome("./chromedriver")
    driver.get(Config.url)
    yield driver
    driver.close()
