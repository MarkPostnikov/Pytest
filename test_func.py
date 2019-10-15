import random
from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def GenKey():
    array = [chr(i) for i in range(65, 91)]

    random.shuffle(array)
    key = ""
    for i in range(5):  # length of key
        key += array.pop()
    return key + "-TEST"


@pytest.fixture()
def browser():
    print("\nstart browser for test..")

    browser = webdriver.Chrome(

    )
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def browser(hidden=False):
    print("\nstart browser for test..")
    global options
    if hidden:

        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        options.add_argument('--no-sandbox')
        options.binary_location = '/usr/bin/google-chrome-stable'

        display = Display(visible=0, size=(1920, 1080))
        display.start()

    browser = webdriver.Chrome(
        executable_path='/home/mark/virtualenv/test_env/tests/driver/chromedriver',
        service_args=['--verbose'] if hidden else None,
        chrome_options=options if hidden else None
    )

    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.fixture
# def wait(browser):
#     wait = WebDriverWait(browser, 10)
#     element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

@pytest.fixture()
def test_login_p(browser):
    browser.get('https://programs.stage.incase.work/')
    browser.find_element_by_id('email-sign-in').send_keys('test1@dev.incase.company')
    browser.find_element_by_id('pass-sign-in').send_keys('Qqqqqqq1')
    browser.find_element_by_xpath('//*[@id="app"]/div/main/div/form/div[3]/button').click()
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "header-content"), "Programs"))
    return browser


# @pytest.fixture(scope='class')
# def test_create_program_limit(test_login_p):
#     browser.get('https://programs.stage.incase.work/')
#     browser.find_element_by_id('email-sign-in').send_keys('test1@dev.incase.company')
#     browser.find_element_by_id('pass-sign-in').send_keys('Qqqqqqq1')
#     browser.find_element_by_xpath('//*[@id="app"]/div/main/div/form/div[3]/button').click()
#     WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "header-content"), "Programs"))


#
# def test_create_program(test_login_p, browser):

def test_create_prog(test_login_p, browser, GenKey):
    browser.maximize_window()
    browser.get('https://programs.stage.incase.work/programs/new')
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Program details"))
    browser.find_element_by_id('program-name').send_keys(GenKey)

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
    browser.find_element_by_id('card-title').send_keys(GenKey)

    browser.find_element_by_id('card-description').send_keys(GenKey)
    browser.find_element_by_id('voucher-value').send_keys('5')
    element = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]')
    browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", element)
    time.sleep(2)
    element.click()
    # browser.execute_script("window.scrollTo(0, 1000);")
    # target = browser.find_element_by_tag_name('Continue')
    # browser.execute_script('arguments[0].scrollIntoView(true);', target)
    # actions = ActionChains(browser)
    # actions.move_to_element(target)
    # actions.perform()
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # html = browser.find_element_by_tag_name('html')
    # html.send_keys(Keys.END)

    # browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]')
    time.sleep(6)
    # ActionChains(browser).move_to_element(elem).perform()
    # time.sleep(5)
    # WebDriverWait(browser, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "button primary large continue")))
    # elem = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]')

    # element = browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]').location_once_scrolled_into_view
    # browser.find_element_by_xpath('//*[@id="app"]/div/div/main/div[2]/button[2]').click()
