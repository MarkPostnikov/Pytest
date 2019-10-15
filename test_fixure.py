import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import math

# url = 'https://programs.stage.incase.work/'
#
# answer = math.log(int(time.time()))


# @pytest.fixture()
# class core:
#     def get(self, browser, href):
#         browser.get(href)
#
#     def __perform(self, browser, elem):
#         try:
#             ActionChains(browser).move_to_element(elem).perform()
#             return True
#         except:
#             time.sleep(2)
#             return True
#
#     def find_element_xp(self, browser, path):
#         return browser.find_element_by_xpath(path)
#
#     def find_element_css(self, browser, path):
#         return browser.find_element_by_css_selector(path)
#
#     def __find_attr(self, browser, path):
#         type = None
#         if isinstance(path, str):
#             type = 'str'
#         elif isinstance(path, list):
#             type = 'list'
#
#         if type == 'str':
#             elem = browser.find_element_by_xpath(path)
#             while not elem:
#                 browser.find_element_by_xpath(path)
#             return elem
#         elif type == 'list':
#             while True:
#                 for p in path:
#                     elem = browser.find_element_by_xpath(p)
#                     if elem:
#                         return elem

# def click(self, browser, path):
#     elem = None
#     while True:
#         try:
#             elem = self.__find_attr(path)
#             elem.click()
#             return elem
#         except:
#             self.__perform(elem)
#
# def set_attr(self, path, value):
#     elem = None
#     while True:
#         try:
#             elem = self.__find_attr(path)
#             elem = self.click(path)
#             elem.send_keys(value)
#             return elem
#         except:
#             self.__perform(elem)


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(
#         executable_path='/home/mark/virtualenv/test_env/tests/driver/chromedriver'
#     )
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.mark.parametrize('url', ["236895/step/1", "236896/step/1",
#                                  "236897/step/1", "236898/step/1",
#                                  "236899/step/1", "236903/step/1",
#                                  "236904/step/1", "236905/step/1"])
# def test_links(url, browser):
#     link = f'https://stepik.org/lesson/{url}'
#     browser.get(link)
#     time.sleep(5)
#     # browser.find_element_by_css_selector('.textarea').click()
#     # time.sleep(2)
#     browser.find_element_by_css_selector('.textarea').send_keys(str(answer))
#     time.sleep(3)
#     browser.find_element_by_css_selector('.attempt__actions > .submit-submission').click()
#     time.sleep(3)
#     print("OK")
#     # corect = browser.find_element_by_xpath('//*[@id="ember1652"]/pre').text("Correct!")
#     corect = browser.find_element_by_css_selector('p.smart-hints__hint').text
#     # browser.find_elements_by_class_name('smart-hints__hint')
#
#     # correct = browser.find_element_by_id('ember1652').tag_name
#     # corect = browser.
#     # corect = browser.find_element_by_xpath("//*[contains(text(),'Correct')]")
#     # assert corect == "Correct!"
#     assert corect == ['Correct!']

    # assert browser.find_element_by_id('ember1682').text == 'Correct!'

# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(
#         executable_path='/home/mark/virtualenv/test_env/tests/driver/chromedriver'
#     )
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# # @pytest.fixture(autouse=True)
# # def prepare_data():
# #     print()
# #     print("preparing some critical data for every test")
#
#
# class TestLogin():
#     def test_user_see_login(self, browser):
#         browser.get(url)
#         browser.find_element_by_xpath('//*[@id="app"]/div/main/div/form/div[3]/a').click()
#         time.sleep(5)
