from pages.profile_edit_page import *
from pages.registration_page import *
from pages.login_page import *
import pytest
from time import sleep
import os


@pytest.mark.smoke
def test_create_user_for_module(browser, delete_user):
    req = RegistrationPage(browser, REGISTRATION_URL)
    req.open()
    req.register_user()
    
    
class TestProfileEditPageInput:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.profile_edit_page = ProfileEditPage(self.browser, PROFILE_EDIT_URL)
        self.profile_edit_page.open()
        login = LoginPage(self.browser, self.browser.current_url)
        login.login_user()

    @pytest.mark.smoke
    @pytest.mark.parametrize('data',
        [{'first_name' : 'First name', 'last_name': '', 'email': '', 'image': '', 'date': ""},
        {'first_name' : '', 'last_name': '', 'email': 'test@mail.ru', 'image': '', 'date': ""},
        {'first_name' : '', 'last_name': '', 'email': '', 'image': '', 'date': "1995-11-09"},
        {'first_name' : '', 'last_name': 'Last_name', 'email': '', 'image': '', 'date': ""},
        {'first_name' : 'First name', 'last_name': 'Last_name', 'email': 'sadof91195@gmail.com',
         'image': os.path.abspath('1.jpg'), 'date': "1995-11-09"},
        {'first_name' : 'First name', 'last_name': 'Last_name', 'email': 'sadof91195@gmail.com',
         'image': os.path.abspath('2.jpg'), 'date': "1995-11-09"},])
    def test_insert_valid_data(self, data):
        self.profile_edit_page.insert_data(data)
        self.profile_edit_page.is_success()
        self.profile_edit_page.chech_data(data)


    @pytest.mark.parametrize('data',
        [pytest.param({'first_name' : 'First name', 'last_name': '', 'email': 'test@', 'image': '', 'date': ""},
        marks=pytest.mark.xfail(reason="can't detect")),
        {'first_name' : 'First name', 'last_name': '', 'email': 'test@a', 'image': '', 'date': ""},
        {'first_name' : 'First name', 'last_name': '', 'email': '', 'image': os.path.abspath('text.txt'), 'date': ""},
        {'first_name' : 'First name', 'last_name': '', 'email': '', 'image': '', 'date': "20-11-2020"},
        pytest.param({'first_name' : 'First name', 'last_name': '', 'email': '', 'image': '', 'date': "1895-11-10"},
        marks=pytest.mark.xfail(reason="birth date validators aren't working")),
        pytest.param({'first_name' : 'First name', 'last_name': '', 'email': '', 'image': '', 'date': "2095-11-10"},
        marks=pytest.mark.xfail(reason="birth date validators aren't working")),])
    def test_insert_invalid_data(self, data):
        self.profile_edit_page.insert_data(data)
        self.profile_edit_page.is_error()