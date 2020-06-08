from .base_page import BasePage
from .locators import ProfileEditPageLocators as PEPL
from selenium import webdriver

PROFILE_EDIT_URL = "http://localhost:8000/accounts/edit/"

class ProfileEditPage(BasePage):

    def is_it_profile_edit(self):
        assert self.browser.current_url == PROFILE_EDIT_URL,\
            f'Url: {self.browser.current_url}, how to be {"http://sadof.pythonanywhere.com/accounts/edit/"}'
        assert self.browser.find_element.text == 'Edit'
        assert self.is_element_present(*PEPL.PROFILE_EDIT_FIRST_NAME)
        assert self.is_element_present(*PEPL.PROFILE_EDIT_LAST_NAME)
        assert self.is_element_present(*PEPL.PROFILE_EDIT_EMAIL)
        assert self.is_element_present(*PEPL.PROFILE_EDIT_IMAGE)
        assert self.is_element_present(*PEPL.PROFILE_EDIT_BIRTH)
        assert self.is_element_present(*PEPL.PROFILE_EDIT_SUBMIT)

    def insert_data(self, data):
        input = self.browser.find_element(*PEPL.PROFILE_EDIT_FIRST_NAME)
        input.clear()
        input.send_keys(data['first_name'])
        input = self.browser.find_element(*PEPL.PROFILE_EDIT_LAST_NAME)
        input.clear()
        input.send_keys(data['last_name'])
        input = self.browser.find_element(*PEPL.PROFILE_EDIT_EMAIL)
        input.clear()
        input.send_keys(data['email'])
        if data['image']: self.browser.find_element(*PEPL.PROFILE_EDIT_IMAGE).send_keys(data['image'])
        input = self.browser.find_element(*PEPL.PROFILE_EDIT_BIRTH)
        input.clear()
        input.send_keys(data['date'])
        self.browser.find_element(*PEPL.PROFILE_EDIT_SUBMIT).click()

    def chech_data(self, data):
        assert self.browser.find_element(*PEPL.PROFILE_EDIT_FIRST_NAME).get_attribute('value') == data['first_name'],\
                self.browser.find_element(*PEPL.PROFILE_EDIT_FIRST_NAME).get_attribute('value')
        assert self.browser.find_element(*PEPL.PROFILE_EDIT_LAST_NAME).get_attribute('value') == data['last_name']
        assert self.browser.find_element(*PEPL.PROFILE_EDIT_EMAIL).get_attribute('value') == data['email']
        assert self.browser.find_element(*PEPL.PROFILE_EDIT_BIRTH).get_attribute('value') == data['date']

    def is_success(self):
        assert self.is_element_present(*PEPL.PROFILE_EDIT_SUCCESS)

    def is_error(self):
        assert self.is_element_present(*PEPL.PROFILE_EDIT_ERROR)