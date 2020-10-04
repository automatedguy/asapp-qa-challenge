from base.setup import ApiConfig


class Urls:

    __SPACE = ' '
    __SPACE_REPLACE = '%20'
    __api_base_url = ApiConfig().get_api_base_url()

    def get_space(self):
        return self.__SPACE

    def get_space_replace(self):
        return self.__SPACE_REPLACE

    def get_api_url(self):
        return self.__api_base_url


class Auth(Urls):

    __USER_REGISTER = '/users/register'
    __USER_LOGIN = '/users/login'
    __USER_LOGOUT = '/users/logout'

    def get_user_register(self):
        return self.get_api_url() + self.__USER_REGISTER

    def get_user_login(self):
        return self.get_api_url() + self.__USER_LOGIN

    def get_user_logout(self):
        return self.get_api_url() + self.__USER_LOGOUT


class Products(Urls):

    __USERNAME_PRODUCTS = '/{username}/products'
    __USERNAME_PRODUCTS_PRODUCT_NAME = '/{username}/products/{product_name}'
    __USERNAME_PRODUCTS_PRODUCT_NAME_ADD = '/{username}/products/{product_name}/add'
    __USERNAME_PRODUCTS_CART = '/{username}/products/cart'
    __USERNAME_PRODUCTS_CART_PRODUCT_NAME_REMOVE = '/{username}/products/cart/{product_name}/remove'
    __USERNAME_PRODUCTS_CART_CHECKOUT = '/{username}/products/cart/checkout'

    def get_username_products(self, username):
        return self.get_api_url() + self.__USERNAME_PRODUCTS\
            .replace('{username}', username)

    def get_user_name_products_product_name(self, username, product_name):
        return self.get_api_url() + self.__USERNAME_PRODUCTS_PRODUCT_NAME\
            .replace('{username}', username)\
            .replace('{product_name}', product_name.replace(self.get_space(), self.get_space_replace()))

    def get_username_products_product_name_add(self, username, product_name):
        return self.get_api_url() + self.__USERNAME_PRODUCTS_PRODUCT_NAME_ADD\
            .replace('{username}', username)\
            .replace('{product_name}', product_name.replace(self.get_space(), self.get_space_replace()))

    def get_username_products_cart(self, username):
        return self.get_api_url() + self.__USERNAME_PRODUCTS_CART\
                   .replace('{username}', username)

    def get_username_products_cart_product_name_remove(self, username, product_name):
        return self.get_api_url() + self.__USERNAME_PRODUCTS_CART_PRODUCT_NAME_REMOVE\
            .replace('{username}', username)\
            .replace('{product_name}', product_name.replace(self.get_space(), self.get_space_replace()))

    def get_username_products_cart_checkout(self, username):
        return self.get_api_url() + self.__USERNAME_PRODUCTS_CART_CHECKOUT\
            .replace('{username}', username)
