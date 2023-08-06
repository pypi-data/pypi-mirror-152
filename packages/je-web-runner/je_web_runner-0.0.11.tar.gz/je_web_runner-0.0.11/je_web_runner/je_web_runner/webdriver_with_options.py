from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.firefox import options
from selenium.webdriver.ie import options
from selenium.webdriver.edge import options
from selenium.webdriver.opera import options

from je_web_runner.utils.exception.exceptions import WebDriverNotFoundException
from je_web_runner.utils.exception.exceptions import OptionsWrongTypeException
from je_web_runner.utils.exception.exceptions import ArgumentWrongTypeException
from je_web_runner.utils.exception.exception_tag import selenium_wrapper_web_driver_not_found_error
from je_web_runner.utils.exception.exception_tag import selenium_wrapper_set_options_error
from je_web_runner.utils.exception.exception_tag import selenium_wrapper_set_argument_error

selenium_options_dict = {
    "chrome": webdriver.chrome.options.Options,
    "chromium": webdriver.chrome.options.Options,
    "firefox": webdriver.firefox.options.Options,
    "opera": webdriver.opera.options.Options,
    "edge": webdriver.edge.options.Options,
    "ie": webdriver.ie.options.Options,
}


def set_webdriver_options_argument(webdriver_name: str, argument_iterable: [list, set]):
    webdriver_options = selenium_options_dict.get(webdriver_name)()
    for i in range(len(argument_iterable)):
        if type(argument_iterable[i]) != str:
            raise ArgumentWrongTypeException(selenium_wrapper_set_argument_error)
        webdriver_options.add_argument(argument_iterable[i])
    return webdriver_options


def set_webdriver_options_capability_wrapper(webdriver_name: str, key_and_vale_dict: dict):
    webdriver_options = selenium_options_dict.get(webdriver_name)()
    if webdriver_options is None:
        raise WebDriverNotFoundException(selenium_wrapper_web_driver_not_found_error)
    if type(key_and_vale_dict) is not dict:
        raise OptionsWrongTypeException(selenium_wrapper_set_options_error)
    for key, value in key_and_vale_dict.items():
        webdriver_options.set_capability(key, value)
    return webdriver_options
