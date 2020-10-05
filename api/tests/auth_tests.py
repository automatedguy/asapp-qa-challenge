from api.services import AuthController
from api.models import *
import random
from base.constants import Msg, Input, StatusCode
from base.setup import BaseApiTest
from base.utils import get_user_id


class AuthTests(BaseApiTest):

    def test_user_register(self):
        username = Input.USERNAME + get_user_id()
        password = Input.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        response = auth_controller.post_user_register(register())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.USER_CREATED_SUCCESSFULLY)
        self.soft_assert(self.assertIn, Msg.USER_CREATED_SUCCESSFULLY, response.text)

        self.assert_all()

    def test_user_login(self):
        username = Input.USERNAME + get_user_id()
        password = Input.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, register_response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.USER_CREATED_SUCCESSFULLY)
        self.soft_assert(self.assertIn, Msg.USER_CREATED_SUCCESSFULLY, register_response.text)

        login_response = auth_controller.post_user_login(register())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, login_response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.LOGIN_SUCCEEDED)
        self.soft_assert(self.assertIn, Msg.LOGIN_SUCCEEDED, login_response.text)

        self.assert_all()

    def test_user_logout(self):
        username = Input.USERNAME + get_user_id()
        password = Input.PASSWORD

        auth_controller = AuthController()
        register = Register(username, password)

        register_response = auth_controller.post_user_register(register())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, register_response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.USER_CREATED_SUCCESSFULLY)
        self.soft_assert(self.assertIn, Msg.USER_CREATED_SUCCESSFULLY, register_response.text)

        login = Login(username, password)
        login_response = auth_controller.post_user_login(login())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, login_response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.LOGIN_SUCCEEDED)
        self.soft_assert(self.assertIn, Msg.LOGIN_SUCCEEDED, login_response.text)

        logout = Logout(username)
        logout_response = auth_controller.post_user_logout(logout())
        self.logger.info(Msg.ASSERTING_STATUS_CODE + str(StatusCode.STATUS_OK))
        self.soft_assert(self.assertEqual, logout_response.status_code, StatusCode.STATUS_OK)
        self.logger.info(Msg.ASSERTING_MESSAGE + Msg.LOGOUT_SUCCEEDED)
        self.soft_assert(self.assertIn, Msg.LOGOUT_SUCCEEDED, logout_response.text)

        self.assert_all()
