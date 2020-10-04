from api.services import AuthController
from api.models import *
import random

from base.setup import BaseApiTest


class AuthTests(BaseApiTest):

    USERNAME = 'username'
    PASSWORD = 'password'

    USER_CREATED_SUCCESSFULLY = 'User created successfully'
    LOGIN_SUCCEEDED = 'Login succeeded.'
    LOGOUT_SUCCEEDED = 'Logout succeeded.'

    def test_user_register(self):
        username = "username" + str(random.randint(100, 1000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        response = auth_controller.post_user_register(register())

        self.soft_assert(self.assertEqual, response.status_code, 200)
        self.soft_assert(self.assertIn, self.USER_CREATED_SUCCESSFULLY, response.text)

        self.assert_all()

    def test_user_login(self):
        username = self.USERNAME + str(random.randint(100, 10000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, self.USER_CREATED_SUCCESSFULLY, register_response.text)

        login_response = auth_controller.post_user_login(register())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, self.LOGIN_SUCCEEDED, login_response.text)

        self.assert_all()

    def test_user_logout(self):
        username = self.USERNAME + str(random.randint(100, 10000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, self.USER_CREATED_SUCCESSFULLY, register_response.text)

        login = Login(username, password)
        login_response = auth_controller.post_user_login(login())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, self.LOGIN_SUCCEEDED, login_response.text)

        logout = Logout(username)
        logout_response = auth_controller.post_user_logout(logout())
        self.soft_assert(self.assertEqual, logout_response.status_code, 200)
        self.soft_assert(self.assertIn, self.LOGOUT_SUCCEEDED, logout_response.text)

        self.assert_all()
