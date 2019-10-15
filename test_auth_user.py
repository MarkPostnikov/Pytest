# import pytest
# from selenium import webdriver
# import time
#
# # url = 'https://programs.stage.incase.work/'
# patches = {
#     'email': {
#         'name': 'email',
#         'path': '//*[@id="email-sign-in"]'
#     },
#     'pass': {
#         'name': 'pass',
#         'path': '//*[@id="pass-sign-in"]',
#         'error': '//*[@id="app"]/div/main/div/form/div[2]/div'
#     }
# }
# url = 'https://programs.stage.incase.work/'
# url2 = 'https://acceptor.stage.incase.work/'
# url3 = 'https://cardholder.stage.incase.work'
#
#

# @pytest.fixture(scope='class')
# class test_enter:
#     def browser(self):
#         print("\nstart browser for test..")
#         browser = webdriver.Chrome(
#             executable_path='/home/mark/virtualenv/test_env/tests/driver/chromedriver'
#         )
#         yield browser
#         print("\nquit browser..")
#         browser.quit()
#
#     def test_user_cardholder(browser):
#         browser.get(url3)
#         email = patches['email']
#         passwd = patches['pass']
#         browser.find_element_by_xpath(email['path']).send_keys('cardholder@dev.incase.company')
#         browser.find_element_by_xpath(passwd['path']).send_keys('Qqqqqqq1')
#         browser.find_element_by_xpath('//*[@id="app"]/div/main/div/form/div[3]/button').click()
#         time.sleep(3)
