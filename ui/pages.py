
import logging

from ui.page_elements import PageElement, LoginPageLocators, AppBarLocators, RegisterPageLocators


class BasePage(object):

    __driver = None

    def __init__(self, driver):
        self.__driver = driver
        self.__logger = logging.getLogger(__name__)

    def __get_driver(self):
        return self.__driver


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.__driver = driver
        self.__username_input = PageElement(self.__driver, LoginPageLocators.USERNAME_INPUT)
        self.__password_input = PageElement(self.__driver, LoginPageLocators.PASSWORD_INPUT)
        self.__login_button = PageElement(self.__driver, LoginPageLocators.LOGIN_BUTTON)
        self.__register_button = PageElement(self.__driver, LoginPageLocators.REGISTER_BUTTON)

    def enter_username(self, username):
        self.__username_input.set_text(username)

    def is_username_visible(self):
        return self.__username_input.is_visible()

    def enter_password(self, password):
        self.__password_input.set_text(password)

    def is_password_visible(self):
        return self.__password_input.is_visible()

    def click_on_log_in_button(self):
        self.__login_button.click()
        return AppMainPage(self.__driver)

    def is_log_in_button_visible(self):
        return self.__login_button.is_visible()

    def click_on_register_button(self):
        self.__register_button.click()
        return RegisterPage(self.__driver)

    def is_register_button_visible(self):
        return self.__register_button.is_visible()


class RegisterPage(BasePage):

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)
        self.__driver = driver
        self.__username_input = PageElement(self.__driver, RegisterPageLocators.USERNAME_INPUT)
        self.__password_input = PageElement(self.__driver, RegisterPageLocators.PASSWORD_INPUT)
        self.__register_button = PageElement(self.__driver, RegisterPageLocators.REGISTER_BUTTON)

    def enter_username(self, username):
        self.__username_input.set_text(username)

    def enter_password(self, password):
        self.__password_input.set_text(password)

    def click_on_register_button(self):
        self.__register_button.click()
        return LoginPage(self.__driver)


class AppMainPage(BasePage):

    def __init__(self, driver):
        super(AppMainPage, self).__init__(driver)
        self.__driver = driver

    def get_app_bar(self):
        return AppBar(self.__driver)

    def get_store_page(self):
        return StorePage(self.__driver)

    def get_cart_page(self):
        return CartPage(self.__driver)


class AppBar(BasePage):

    def __init__(self, driver):
        super(AppBar, self).__init__(driver)
        self.__driver = driver
        self.__store_tab = PageElement(self.__driver, AppBarLocators.STORE_TAB)
        self.__cart_tab = PageElement(self.__driver, AppBarLocators.CART_TAB)
        self.__log_out_tab = PageElement(self.__driver, AppBarLocators.LOG_OUT_TAB)

    def click_on_store_tab(self):
        self.__store_tab.click()
        return StorePage(self.__driver)

    def is_store_tab_visible(self):
        return self.__store_tab.is_visible()

    def click_on_cart_tab(self):
        self.__cart_tab.click()
        return CartPage(self.__driver)

    def is_cart_tab_visible(self):
        return self.__cart_tab.is_visible()

    def click_on_log_out_tab(self):
        self.__log_out_tab.click()
        return LoginPage(self.__driver)

    def is_log_out_tab_visible(self):
        return self.__log_out_tab.is_visible()


class StorePage(BasePage):

    def __init__(self, driver):
        super(StorePage, self).__init__(driver)
        self.__driver = driver


class ProductCard(BasePage):

    def __init__(self, driver):
        super(ProductCard, self).__init__(driver)
        self.__driver = driver


class CartPage(BasePage):

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)
        self.__driver = driver
