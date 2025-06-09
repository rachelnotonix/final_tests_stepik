from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
from .locators import LoginPageLocators, ProductPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_no_items_in_cart(self):
        assert (
            "Your basket is empty"
            in self.browser.find_element(
                By.XPATH, "//p[contains(text(), 'Your basket is empty.')]"
            ).text
        )
