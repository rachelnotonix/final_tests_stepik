from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.XPATH, "//a[@id='registration_link']")

class LoginPageLocators():

    LOGIN_PAGE = (By.XPATH, "//title[contains(text(), 'Login or register')]")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")