import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3
from pages.registration_page import *


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language to use")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")

    browser.quit()


@pytest.fixture(scope="module")
def delete_user(request):
    conn = sqlite3.connect('C:/Users/Sadof/PycharmProjects/all_in_one/venv/all_in_one/db.sqlite3')
    cursor = conn.cursor()
    yield delete_user
    sql = "DELETE FROM auth_user"
    cursor.execute(sql)
    conn.commit()
    conn.close()

@pytest.fixture(scope="module")
def create_user(browser):
    conn = sqlite3.connect('C:/Users/Sadof/PycharmProjects/all_in_one/venv/all_in_one/db.sqlite3')
    cursor = conn.cursor()
    yield delete_user
    sql = "DELETE FROM auth_user"
    cursor.execute(sql)
    conn.commit()
    conn.close()



@pytest.fixture(scope="class")
def db_connection(request):
    conn = sqlite3.connect('C:/Users/Sadof/PycharmProjects/all_in_one/venv/all_in_one/db.sqlite3')
    cursor = conn.cursor()
    yield (conn,cursor)
    conn.close()
