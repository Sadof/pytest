from pages.registration_page import RegistrationPage
from pages.index_page import IndexPage
from pages.profile_edit_page import ProfileEditPage
import pytest
from time import sleep
import random
import sqlite3

REGISTRATIONPAGE_URL = 'http://localhost:8000/accounts/registration/'


def test_check_input_fields(browser):
    registration_page = RegistrationPage(browser, REGISTRATIONPAGE_URL)
    registration_page.open()
    registration_page.is_it_registration_page()


class TestRegistrationInsertDifferentData:

    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, db_connection):
        self.browser = browser
        self.conn, self.cursor = (db_connection)
        self.registration_page = RegistrationPage(self.browser, REGISTRATIONPAGE_URL, self.cursor)
        self.registration_page.open()
        self.registration_page.is_it_registration_page()
        yield
        sql = "DELETE FROM auth_user"
        self.cursor.execute(sql)
        self.conn.commit()

    @pytest.mark.smoke
    def test_is_it_registration_page(self):
        self.registration_page.is_it_registration_page()

    @pytest.mark.smoke
    @pytest.mark.xfail(reason="Wrong redirect URL")
    def test_insert_valid_data(self):
        self.registration_page.register_user()
        self.registration_page.user_created()
        profile_edit_page = ProfileEditPage(self.browser, self.browser.current_url)
        profile_edit_page.is_it_profile_edit()

    @pytest.mark.parametrize('password',['Quest123',
                                        '534634634534',
                                         'Random2',
                                         'qwerty123',])
    def test_insert_invalid_password(self, password):
        self.registration_page.register_user(username='Quest', password=password)
        self.registration_page.is_an_error()
        self.registration_page.user_not_created()

    def test_insert_invalid_username(self):
        self.registration_page.register_user("Qeust{", "Sadof123")

    # def test_insert_invalid_data_short_password(self, browser):
    #     index_page = IndexPage(browser, INDEXPAGE_URL)
    #     index_page.open()
    #     index_page.go_to_registration_page()
    #     registration_page = RegistrationPage(browser, browser.current_url)
    #     registration_page.register_user(username='username34534',password='Random2')
    #     registration_page.is_an_error()
    #
    # def test_insert_invalid_data_numeric_password(self, browser):
    #     index_page = IndexPage(browser, INDEXPAGE_URL)
    #     index_page.open()
    #     index_page.go_to_registration_page()
    #     registration_page = RegistrationPage(browser, browser.current_url)
    #     registration_page.register_user(username='username34534',password='534634634534')
    #     registration_page.is_an_error()
    #
    #
    # def test_insert_invalid_data_common_password(self, browser):
    #     index_page = IndexPage(browser, INDEXPAGE_URL)
    #     index_page.open()
    #     index_page.go_to_registration_page()
    #     registration_page = RegistrationPage(browser, browser.current_url)
    #     registration_page.register_user(username='username34534', password='qwerty123')
    #     registration_page.is_an_error()