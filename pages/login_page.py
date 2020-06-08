from .base_page import BasePage
from .locators import LoginPageLocators as LPL
from selenium import webdriver

LOGIN_PAGE_URL = 'http://localhost:8000/accounts/login/'

class LoginPage(BasePage):
    
    def is_it_login_page(self):
        assert self.browser.current_url == LOGIN_PAGE_URL
        assert self.is_element_present(*LPL.LOGIN_BUTTON)
        assert self.is_element_present(*LPL.LOGIN_PASSWORD)
        assert self.is_element_present(*LPL.LOGIN_USERNAME)

    def login_user(self, username= 'Quest', password = 'Sadof123'):
        self.browser.find_element(*LPL.LOGIN_USERNAME).send_keys(username)
        self.browser.find_element(*LPL.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LPL.LOGIN_BUTTON).click()


    def is_an_error(self):
        assert self.browser.find_element(\
            *LPL.LOGIN_ALERT).text == "Your username and password didn't match. Please try again.", \
            self.browser.find_element(*LPL.LOGIN_ALERT).text