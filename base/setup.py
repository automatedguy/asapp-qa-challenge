import configparser

_URLS_INI_ = 'urls.ini'
_PROTOCOL_ = 'http'


class TestConfig:

    _config = configparser.ConfigParser()
    _config.read(_URLS_INI_)


class ApiConfig(TestConfig):

    def __init__(self):
        self._api_url = self._config['API']['URL']
        self._api_port = self._config['API']['PORT']

    def get_api_base_url(self):
        return _PROTOCOL_ + '://' + self._api_url + ':' + self._api_port


class UiConfig(TestConfig):

    def __init__(self):
        self._ui_url = self._config['UI']['URL']
        self._ui_port = self._config['UI']['PORT']

    def get_ui_base_url(self):
        return _PROTOCOL_ + '://' + self._ui_url + ':' + self._ui_port
