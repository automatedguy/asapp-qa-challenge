from api.services import AuthController
from api.models import *
import random
from base.constants import Messages, Inputs
from base.setup import BaseApiTest
from base.utils import get_user_id


class AuthTests(BaseApiTest):

    def test_user_register(self):
        username = Inputs.USERNAME + get_user_id()
        password = Inputs.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        response = auth_controller.post_user_register(register())

        self.soft_assert(self.assertEqual, response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.USER_CREATED_SUCCESSFULLY, response.text)

        self.assert_all()

    def test_user_login(self):
        username = Inputs.USERNAME + get_user_id()
        password = Inputs.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.USER_CREATED_SUCCESSFULLY, register_response.text)

        login_response = auth_controller.post_user_login(register())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.LOGIN_SUCCEEDED, login_response.text)

        self.assert_all()

    def test_user_logout(self):
        username = Inputs.USERNAME + get_user_id()
        password = Inputs.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.USER_CREATED_SUCCESSFULLY, register_response.text)

        login = Login(username, password)
        login_response = auth_controller.post_user_login(login())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.LOGIN_SUCCEEDED, login_response.text)

        logout = Logout(username)
        logout_response = auth_controller.post_user_logout(logout())
        self.soft_assert(self.assertEqual, logout_response.status_code, 200)
        self.soft_assert(self.assertIn, Messages.LOGOUT_SUCCEEDED, logout_response.text)

        self.assert_all()
