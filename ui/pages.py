
import logging


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    pass


class AppMainPage(BasePage):
    pass


class AppBar(BasePage):
    pass


class ProductsPage(BasePage):
    pass


class ProductCard(BasePage):
    pass
