from base.setup import BaseUiTest
from ui.pages import LoginPage
from api.services import AuthController
from api.models import *
import random


class LoginTests(BaseUiTest):

    def test_login(self):
        username = self.USERNAME + str(random.randint(100, 1000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)
        response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, response.status_code, 200)

        login_page = LoginPage(self.get_driver())
        login_page.enter_username(username)
        login_page.enter_password(password)
        app_main_page = login_page.click_on_log_in_button()

        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_store_tab_visible())
        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_cart_tab_visible())
        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_log_out_tab_visible())

        self.assert_all()

    def test_logout(self):
        username = self.USERNAME + str(random.randint(100, 1000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)
        response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, response.status_code, 200)

        login_page = LoginPage(self.get_driver())
        login_page.enter_username(username)
        login_page.enter_password(password)
        app_main_page = login_page.click_on_log_in_button()

        login_page = app_main_page.get_app_bar().click_on_log_out_tab()

        self.soft_assert(self.assertTrue, login_page.is_username_visible())
        self.soft_assert(self.assertTrue, login_page.is_password_visible())
        self.soft_assert(self.assertTrue, login_page.is_log_in_button_visible())
        self.soft_assert(self.assertTrue, login_page.is_register_button_visible())

        self.assert_all()

    def test_register(self):
        username = self.USERNAME + str(random.randint(100, 1000))
        password = self.PASSWORD

        login_page = LoginPage(self.get_driver())
        register_page = login_page.click_on_register_button()
        register_page.enter_username(username)
        register_page.enter_password(password)
        login_page_register = register_page.click_on_register_button()

        login_page_register.enter_username(username)
        login_page_register.enter_password(password)
        app_main_page = login_page_register.click_on_log_in_button()

        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_store_tab_visible())
        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_cart_tab_visible())
        self.soft_assert(self.assertTrue, app_main_page.get_app_bar().is_log_out_tab_visible())

        self.assert_all()
