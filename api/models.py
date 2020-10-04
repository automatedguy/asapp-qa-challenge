import json


class Model:

    _model = None


class Register(Model):

    def __init__(self, username, password):
        self._model = json.dumps(
            {
                "username": username,
                "password": password
             }
        )

    def __call__(self):
        return self._model


class Login(Model):

    def __init__(self, username, password):
        self._model = json.dumps(
            {
                "username": username,
                "password": password
             }
        )

    def __call__(self):
        return self._model


class Logout(Model):

    def __init__(self, username):
        self._model = json.dumps(
            {
                "username": username
            }
        )

    def __call__(self):
        return self._model


class Add(Model):

    def __init__(self, quantity):
        self._model = json.dumps(
            {
                "quantity": quantity
            }
        )

    def __call__(self):
        return self._model

