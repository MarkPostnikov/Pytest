from BaseApp import Core
from core.constants.locators import SearchLocators


# class word:
#     email_owner = 'test1@dev.incase.company'
#     password_owner = 'Qqqqqqq1'
#     email_acceptor = 'acceptorman@dev.incase.company'
#     password_acceptor = 'Qqqqqqq1'
#     email_cardholder = 'cardholder@dev.incase.company'
#     password_cardholder = 'Qqqqqqq1'

class SearchHelper(Core):

    def enter_input(self, word, locator=None):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self, locator):
        return self.find_element(locator=locator, wait=2).click()
