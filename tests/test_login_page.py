from pages.login_page import LoginPage
from pages.registration_page import *
import pytest
from time import sleep


LOGINPAGE_URL = 'http://localhost:8000/accounts/login/'

@pytest.mark.smoke
def test_create_user_for_module(browser, delete_user):
    req = RegistrationPage(browser, REGISTRATION_URL)
    req.open()
    req.register_user()

class TestLoginInsertDifferentData:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.login_page = LoginPage(self.browser, LOGINPAGE_URL)
        self.login_page.open()

    @pytest.mark.smoke
    def test_login_page_layout(self):
        self.login_page.is_it_login_page()


    def test_login_user_with_correct_data(self):
        self.login_page.login_user()


    @pytest.mark.parametrize('data',[{'username': 'Quest1', 'password' : 'Sadof123'},
                                     {'username': 'Quest', 'password' : 'Sadof124'},
                                     {'username': 'Quest1', 'password' : 'Sadof124'},])
    def test_login_user_with_incorrect_data(self, data):

        self.login_page.login_user(data['username'], data['password'])
        self.login_page.is_an_error()