from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageElement(object):

    __locator = None
    __driver = None
    __element = None

    MAX_RETRY = 30
    MAX_WAIT = 3
    DELAY = 1

    def __init__(self, driver, locator):
        self.__driver = driver
        self.__locator = locator

    def click(self):
        self.__element = self._wait_for_element(self.__locator)
        self.__element.click()

    def set_text(self, text):
        self.__element = self._wait_for_element(self.__locator)
        self.__element.send_keys(text)

    def is_visible(self):
        self.__element = self._wait_for_element(self.__locator)
        return self.__element.is_displayed()

    def _wait_for_element(self, locator):
        count = 0
        element = None
        while count < self.MAX_RETRY and element is None:
            try:
                element = WebDriverWait(self.__driver, self.MAX_RETRY).until(
                    EC.element_to_be_clickable((By.XPATH, locator))
                )
            except StaleElementReferenceException:
                sleep(self.MAX_WAIT)
                count += 1
        sleep(self.DELAY)
        return element


class LoginPageLocators(object):

    USERNAME_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//span[@class="MuiButton-label" and text()="Log In"]/ancestor::button'
    REGISTER_BUTTON = '//span[@class="MuiButton-label" and text()="Register"]/ancestor::button'


class RegisterPageLocators(object):

    USERNAME_INPUT = '//input[@id="register-username"]'
    PASSWORD_INPUT = '//input[@id="register-password"]'
    REGISTER_BUTTON = '(//span[@class="MuiButton-label" and text()="Register"])[2]/ancestor::button'


class IncorrectCredentialsPopUpLocators(object):

    INCORRECT_CREDENTIALS_MESSAGE = ''
    CLOSE_BUTTON = ''


class AppBarLocators(object):

    STORE_TAB = '//span[@class="MuiTab-wrapper" and text()="Store"]/ancestor::button'
    CART_TAB = '//span[@class="MuiTab-wrapper" and text()="Cart"]/ancestor::button'
    LOG_OUT_TAB = '//span[@class="MuiTab-wrapper" and text()="Log Out"]/ancestor::button'


class ProductPageLocator(object):

    PRODUCT_CARDS = ''


class ProductCardLocators(object):

    ADD_TO_CART_BUTTON = ''
    IN_STOCK_LABEL = ''
    QUANTITY_SELECT = ''


class AddedToCartLocator(object):

    ADDED_TO_CART_MESSAGE = ''
    CLOSE_BUTTON = ''
