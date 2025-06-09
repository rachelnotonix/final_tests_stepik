from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, ProductPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    pass