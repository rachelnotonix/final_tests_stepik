from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()