from selenium import webdriver
from .base_page import BasePage
from .locators import RegistrationPageLocators as RPL
import pytest


REGISTRATION_URL = "http://localhost:8000/accounts/registration/"

class RegistrationPage(BasePage):


    def is_it_registration_page(self):
        title = self.browser.find_element(*RPL.TITLE).text
        assert self.browser.current_url == REGISTRATION_URL, f"{self.browser.current_url}, {REGISTRATION_URL}"
        assert title == "Registration", f"Title  = {title}, suppose to be 'Registration'"
        assert self.is_element_present(*RPL.REGISTRATION_USERNAME)
        assert self.is_element_present(*RPL.REGISTRATION_PASSWORD)
        assert self.is_element_present(*RPL.REGISTRATION_PASSWORD_CONFIRM)
        assert self.is_element_present(*RPL.REGISTRATION_BUTTON)


    def register_user(self, username=  'Quest', password = 'Sadof123', conf_password=''):
        conf_password = conf_password if conf_password else password
        self.browser.find_element(*RPL.REGISTRATION_USERNAME).send_keys(username)
        self.browser.find_element(*RPL.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*RPL.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*RPL.REGISTRATION_BUTTON).click()

    def is_an_error(self):
        err_messages = ['This password is entirely numeric.',
                        'This password is too common.',
                        'The password is too similar to the username.',
                        'This password is too short. It must contain at least 8 characters.',
                        "The two password fields didn't match."]
        assert self.browser.find_element(*RPL.REGISTRATION_ALERT).text in err_messages

    def user_created(self):
        sql = "SELECT count(*) FROM auth_user"
        count = self.cursor.execute(sql).fetchone()[0]
        assert count == 1, count
        
    def user_not_created(self):
        sql = "SELECT count(*) FROM auth_user"
        count = self.cursor.execute(sql).fetchone()[0]
        assert count == 0, count