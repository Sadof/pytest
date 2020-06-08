from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators as BPL


class BasePage:
    def __init__(self, browser, url, cursor=None, timeout=2):
        self.browser = browser
        self.url = url
        self.cursor = cursor
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        btn = self.browser.find_element(*BPL.LOGIN_BUTTON)
        btn.click()

    def go_to_registration_page(self):
        btn = self.browser.find_element(*BPL.REGISTRATION_BUTTON)
        btn.click()

    def is_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def should_contain_login_link(self):
        assert self.is_element_present(*BPL.LOGIN_BUTTON)

    def should_contain_registration_link(self):
        assert self.is_element_present(*BPL.REGISTRATION_BUTTON)


    def should_not_contain_create_post_button(self):
        self.browser.find_element(*BPL.BLOG_BUTTON).click()
        assert self.is_not_element_present(*BPL.POST_CREATE_BUTTON), self.browser.find_element(*BPL.POST_CREATE_BUTTON).text

    def should_not_contain_create_test_button(self):
        assert self.is_not_element_present(*BPL.POST_CREATE_BUTTON), self.browser.find_element(
            *BPL.POST_CREATE_BUTTON).text