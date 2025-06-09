from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import browser
from .locators import LoginPageLocators, ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_product_link(self):
        assert "catalogue/" in self.browser.current_url, "This isn't a product link"

    def should_be_correct_name_of_product_in_basket(self):
        self.product_name = self.browser.find_element(By.XPATH, "//h1")
        assert self.product_name.text == self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_ITEM).text, "The name of the item is incorrect"

    def should_be_correct_price_in_basket(self):
        self.product_price = self.browser.find_element(By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")
        assert self.product_price.text == self.browser.find_element(*ProductPageLocators.VALUE_OF_BASKET).text, "The price is incorrect"