import json


class Model:

    _data = None


class Register(Model):

    def __init__(self, username, password):
        self._data = json.dumps(
            {
                "username": username,
                "password": password
             }
        )

    def __call__(self):
        return self._data


class Login(Model):

    def __init__(self, username, password):
        self._data = json.dumps(
            {
                "username": username,
                "password": password
             }
        )

    def __call__(self):
        return self._data


class Logout(Model):

    def __init__(self, username):
        self._data = json.dumps(
            {
                "username": username
            }
        )

    def __call__(self):
        return self._data


class Add(Model):

    def __init__(self, quantity):
        self._data = json.dumps(
            {
                "quantity": quantity
            }
        )

    def __call__(self):
        return self._data

