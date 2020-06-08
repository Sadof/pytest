from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '#navbarSupportedContent form input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#navbarSupportedContent form button')
    LOGIN_BUTTON = (By.LINK_TEXT, 'Login')
    REGISTRATION_BUTTON = (By.LINK_TEXT, 'Registration')
    POSTS_BUTTON = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='Posts']")
    POST_CREATE_BUTTON = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='Create post']")
    TEST_CREATE_BUTTON = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='Create']")
    TEST_MY_TEST_BUTTON = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='My tests']")
    PROFILE_LINK = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='My profile']")
    PROFILE_EDIT_LINK = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='Edit']")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'navbar-nav')]//*[text()='Logout']")
    BLOG_BUTTON = (By.LINK_TEXT, 'Blog')
    TESTS_BUTTON = (By.LINK_TEXT, 'Tests')

# Locators for this page is really bad and ununique cuz of my layuot (for examplpe 2 h1 tags)
class IndexPageLocators:
    TITLE = (By.XPATH, '/html/body/div/div/div/h1[2]')


class RegistrationPageLocators:
    TITLE = (By.CSS_SELECTOR, '.row h1')
    REGISTRATION_USERNAME = (By.CSS_SELECTOR, '.row form #id_username')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '.row form #id_password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '.row form #id_password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".row form input[type='submit'][value='Registrate']")
    REGISTRATION_ALERT = (By.CSS_SELECTOR, '.alert.alert-danger')




class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, '.row form #id_username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR,'.row form #id_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".row form input[type='submit'][value='login']")
    LOST_PASSWORD = (By.LINK_TEXT, 'Lost password?')
    LOGIN_ALERT = (By.CSS_SELECTOR, '.row p')


class ProfileEditPageLocators:
    PROFILE_EDIT_TITLE = (By.CSS_SELECTOR, '.row p')
    PROFILE_EDIT_SUCCESS = (By.CSS_SELECTOR, 'ul.messages > li.success')
    PROFILE_EDIT_ERROR = (By.CSS_SELECTOR, 'ul.messages > li.error')
    PROFILE_EDIT_FIRST_NAME = (By.ID, 'id_first_name')
    PROFILE_EDIT_LAST_NAME = (By.ID, 'id_last_name')
    PROFILE_EDIT_EMAIL = (By.ID, 'id_email')
    PROFILE_EDIT_IMAGE = (By.XPATH, "//input[@type='file']")
    PROFILE_EDIT_BIRTH = (By.ID, 'id_date_of_birth')
    PROFILE_EDIT_SUBMIT = (By.XPATH, "//input[@type='submit' and @value='Save changes']")