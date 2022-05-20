from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from config import Config
class Visible(visibility_of_element_located):
    def __call__(self, driver):
        res = super().__call__(driver)
        if isinstance(res, WebElement):
            return res.is_enabled()
        return False


def demo(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        obj_wait = WebDriverWait(instance.driver, Config.max_time)
        obj_class = Visible(locator)
        obj_wait.until(obj_class)
        return func(*args, **kwargs)
    return wrapper
