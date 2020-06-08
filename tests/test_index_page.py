from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import pytest
from time import sleep



INDEXPAGE_URL = 'http://localhost:8000/'


@pytest.mark.smoke
class TestIndexPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.index_page = IndexPage(self.browser, INDEXPAGE_URL)
        self.index_page.open()

    def test_open_index_page(self):
        self.index_page.is_it_index_page()

    def test_authorized_user_can_see_login_link(self):
        self.index_page.should_contain_login_link()

    def test_authorized_user_press_login_link(self):
        self.index_page.go_to_login_page()
        login_page =LoginPage(self.browser, self.browser.current_url)
        login_page.is_it_login_page()


    def test_authorized_user_can_see_registration_link(self):
        self.index_page.should_contain_registration_link()

        
    def test_authorized_user_press_registration_link(self):
        self.index_page.go_to_registration_page()
        registration_page = RegistrationPage(self.browser, self.browser.current_url)
        registration_page.is_it_registration_page()
        

    def test_authorized_user_can_not_see_create_post_button(self):
        self.index_page.should_not_contain_create_post_button()

    def test_authorized_user_can_not_see_create_test_button(self):
        self.index_page.should_not_contain_create_test_button()
