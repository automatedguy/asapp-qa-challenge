from api.resources.urls import Auth
import requests


class Service:

    _urls = Auth
    _requests = requests

    def _get(self, url):
        return self.__requests.get(url)

    def _post(self, url, post_data):
        return self.__requests.post(url, post_data)


class AuthController(Service):

    def post_user_register(self, body):
        self._post(self._urls.get_user_register, body)

    def post_user_login(self, body):
        self._post(self._urls.get_user_login, body)

    def post_user_logout(self, body):
        self._post(self._urls.get_user_logout, body)


class ProductController(Service):

    def get_username_products(self, username):
        pass

    def get_username_products_product_name(self, username, product_name):
        pass

    def post_username_products_product_name_add(self, username, product_name):
        pass

    def get_username_products_cart(self, username):
        pass

    def post_username_products_cart_product_name_remove(self, username, product_name):
        pass

    def post_username_products_cart_checkout(self, username):
        pass
