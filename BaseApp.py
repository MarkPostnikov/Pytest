from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Core:
    def __init__(self, driver):
        self.driver = driver
        self.base_url_owner = 'https://programs.stage.incase.work/'
        self.base_url_acceptor = 'https://acceptor.stage.incase.work/'
        self.base_url_cardholder = 'https://cardholder.stage.incase.work/'

    def find_element(self, locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site_owner(self):
        return self.driver.get(self.base_url_owner)

    def go_to_site_acceptor(self):
        return self.driver.get(self.base_url_acceptor)

    def go_to_site_cardholder(self):
        return self.driver.get(self.base_url_cardholder)

    def __perform(self, elem):
        try:
            ActionChains(self.driver).move_to_element(elem).perform()
            return True
        except:
            time.sleep(2)
            return True

    def find_element_xp(self, path):
        return self.driver.find_element_by_xpath(path)

    def find_element_css(self, path):
        return self.driver.find_element_by_css_selector(path)

    def __find_attr(self, path):
        type = None
        if isinstance(path, str):
            type = 'str'
        elif isinstance(path, list):
            type = 'list'

        if type == 'str':
            elem = self.driver.find_element_by_xpath(path)
            while not elem:
                self.driver.find_element_by_xpath(path)
            return elem
        elif type == 'list':
            while True:
                for p in path:
                    elem = self.driver.find_element_by_xpath(p)
                    if elem:
                        return elem

    def click(self, path):
        elem = None
        while True:
            try:
                elem = self.__find_attr(path)
                elem.click()
                return elem
            except:
                self.__perform(elem)

    def set_attr(self, path, value):
        elem = None
        while True:
            try:
                elem = self.__find_attr(path)
                elem = self.click(path)
                elem.send_keys(value)
                return elem
            except:
                self.__perform(elem)
