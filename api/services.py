from api.urls import *
import requests


class Service:

    __requests = requests

    __headers = {
        "accept": "application/xml",
        "Content-Type": "application/json"
    }

    def _get(self, url):
        return self.__requests.get(url)

    def _post(self, url, body):
        return self.__requests.post(url, data=body, headers=self.__headers)


class AuthController(Service):

    __urls = Auth()

    def post_user_register(self, body):
        return self._post(self.__urls.get_user_register(), body)

    def post_user_login(self, body):
        return self._post(self.__urls.get_user_login(), body)

    def post_user_logout(self, body):
        return self._post(self.__urls.get_user_logout(), body)


class ProductController(Service):

    __urls = Products()

    def get_username_products(self, username):
        return self._get(self.__urls.get_username_products(username))

    def get_username_products_product_name(self, username, product_name):
        return self._get(self.__urls.get_user_name_products_product_name(username, product_name))

    def post_username_products_product_name_add(self, username, product_name, body):
        return self._post(self.__urls.get_username_products_product_name_add(username, product_name), body)

    def get_username_products_cart(self, username):
        return self._get(self.__urls.get_username_products_cart(username))

    def post_username_products_cart_product_name_remove(self, username, product_name, body):
        return self._post(self.__urls.get_username_products_cart_product_name_remove(username, product_name), body)

    def post_username_products_cart_checkout(self, username, body):
        return self._post(self.__urls.get_username_products_cart_checkout(username), body)
