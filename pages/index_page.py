from selenium import webdriver
from .base_page import BasePage
from .locators import IndexPageLocators as IPL

INDEX_URL = 'http://localhost:8000/'

class IndexPage(BasePage):

    def is_it_index_page(self):
        assert self.browser.current_url == INDEX_URL
        assert "Приветствую на сайте" in self.browser.find_element(*IPL.TITLE).text
