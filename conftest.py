import time

import pytest
from pyvirtualdisplay import Display
from selenium import webdriver

from BasePages import SearchHelper
from core.constants.locators import SearchLocators
from test_Singin import email_owner, password_owner


@pytest.fixture(scope='session')
def browser(hidden=False):
    print("\nstart browser for test..")

    if hidden:
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        options.add_argument('--no-sandbox')
        options.binary_location = '/usr/bin/google-chrome-stable'

        display = Display(visible=0, size=(1920, 1080))
        display.start()

    driver = webdriver.Chrome(
        executable_path='/home/mark/virtualenv/test_env/tests/driver/chromedriver',
        service_args=['--verbose'] if hidden else None,

    )

    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope='function')
def test_singin(browser):
    incase_main_page = SearchHelper(browser)
    incase_main_page.go_to_site_owner()
    incase_main_page.enter_input(email_owner, SearchLocators.Locator_email)
    incase_main_page.enter_input(password_owner, SearchLocators.Locator_password)
    incase_main_page.click_on_the_search_button(SearchLocators.Locator_Button)
    time.sleep(4)
    return test_singin