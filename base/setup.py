import configparser
import logging
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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


class BaseUiTest(unittest.TestCase):

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    __ui_base_url = UiConfig().get_ui_base_url()
    __driver = ''

    @classmethod
    def setUpClass(cls):
        """Run our `setUp` method on inherited classes, """
        if cls is not BaseUiTest and cls.setUp is not BaseUiTest.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseUiTest.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride

    def _set_chrome(self):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_driver(self):
        return self.__driver

    def setUp(self):
        self._set_chrome()
        self.get_driver().maximize_window()
        self.get_driver().get(self.__ui_base_url)

    def tearDown(self):
        self.logger.info('-----')
        self.get_driver().quit()
