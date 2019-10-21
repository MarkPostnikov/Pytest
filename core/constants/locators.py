from selenium.webdriver.common.by import By


class SearchLocators:
    Locator_email = (By.ID, "email-sign-in")
    Locator_password = (By.ID, "pass-sign-in")
    Locator_Button = (By.XPATH, '//*[@id="app"]/div/main/div/form/div[3]/button')

    class