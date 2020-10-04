
class PageElement(object):

    __locator = ''
    __driver = None
    __element = None

    def __init__(self, locator, driver):
        self.__locator = locator
        self.__driver = driver

    def __call__(self):
        self.__element = self.__driver.find_element_by_xpath(self.__locator)

    def click(self):
        self.__element.click()

    def set_text(self, text):
        self.__element.send_keys(text)


class LoginPageLocators(object):

    USERNAME_INPUT = ''
    PASSWORD_INPUT = ''
    LOGIN_BUTTON = ''
    REGISTER_BUTTON = ''


class AppBarLocators(object):

    STORE_TAB = ''
    CART_TAB = ''
    LOG_OUT_TAB = ''


class ProductPageLocator(object):

    PRODUCT_CARDS = ''


class ProductCardLocators(object):

    ADD_TO_CART_BUTTON = ''
    IN_STOCK_LABEL = ''
    QUANTITY_SELECT = ''


class AddedToCartLocator(object):

    ADDED_TO_CART_MESSAGE = ''
    CLOSE_BUTTON = ''
