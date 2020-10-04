import softest

from api.services import AuthController
from api.models import *
import random


class AuthTests(softest.TestCase):

    USERNAME = 'username'
    PASSWORD = 'password'

    def test_user_register(self):
        username = "username" + str(random.randint(100, 1000))
        password = "password"

        auth_controller = AuthController()
        register = Register(username, password)

        response = auth_controller.post_user_register(register())

        self.soft_assert(self.assertEqual, response.status_code, 200)
        self.soft_assert(self.assertIn, 'User created successfully', response.text)

        self.assert_all()

    def test_user_login(self):
        username = self.USERNAME + str(random.randint(100, 10000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, 'User created successfully', register_response.text)

        login_response = auth_controller.post_user_login(register())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, 'Login succeeded.', login_response.text)

        self.assert_all()

    def test_user_logout(self):
        username = self.USERNAME + str(random.randint(100, 10000))
        password = self.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.soft_assert(self.assertEqual, register_response.status_code, 200)
        self.soft_assert(self.assertIn, 'User created successfully', register_response.text)

        login = Login(username, password)
        login_response = auth_controller.post_user_login(login())
        self.soft_assert(self.assertEqual, login_response.status_code, 200)
        self.soft_assert(self.assertIn, 'Login succeeded.', login_response.text)

        logout = Logout(username)
        logout_response = auth_controller.post_user_logout(logout())
        self.soft_assert(self.assertEqual, logout_response.status_code, 200)
        self.soft_assert(self.assertIn, 'Logout succeeded.', logout_response.text)

        self.assert_all()
