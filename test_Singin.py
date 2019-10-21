from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from BasePages import SearchHelper
from core.constants.locators import SearchLocators
import time
import pytest

email_owner = 'test1@dev.incase.company'
password_owner = 'Qqqqqqq1'
email_acceptor = 'acceptorman@dev.incase.company'
password_acceptor = 'Qqqqqqq1'
email_cardholder = 'cardholder@dev.incase.company'
password_cardholder = 'Qqqqqqq1'


#
# def test_singin(browser):
#     incase_main_page = SearchHelper(browser)
#     incase_main_page.go_to_site_owner()
#     incase_main_page.enter_input(email_owner, SearchLocators.Locator_email)
#     incase_main_page.enter_input(password_owner, SearchLocators.Locator_password)
#     incase_main_page.click_on_the_search_button(SearchLocators.Locator_Button)
#     time.sleep(4)


def test_create_prog(browser, test_singin):
    browser.get('https://programs.stage.incase.work/programs/new')
    time.sleep(2)
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Program details"))
    browser.find_element_by_id('program-name').send_keys("erererrwr")

    browser.find_element_by_id('program-description').send_keys('Test1, erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrerTest1, '
                                                                'erewrerTest1, erewrerTest1, erewrer')

    browser.find_element_by_css_selector('#app > div > div > main > div.content > button').click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "heading-4"), "Choose Card Type"))

    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div/main/div[2]/div/div[1]/div[1]').click()

    browser.find_element_by_css_selector(
        '#app > div > div > main > div.wrapper-steps > button.button.primary.large.continue').click()

    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "heading-4"), "Card design"))
    file_imput = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/div[1]/div[3]/input')
    file_imput.send_keys('/home/mark/Downloads/img')
    WebDriverWait(browser, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "button primary-outline large btn")))
    browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/div[1]/button[1]').click()
    browser.find_element_by_id('card-title').send_keys("retretrete")

    browser.find_element_by_id('card-description').send_keys("ereretrt")
    browser.find_element_by_id('voucher-value').send_keys('5')
    element = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]')
    browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", element)
    time.sleep(2)
    element.click()
