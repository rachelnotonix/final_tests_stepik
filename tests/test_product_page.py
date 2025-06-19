import time, math, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.locators import ProductPageLocators
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_link()
    add_basket = browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
    add_basket.click()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_of_product_in_basket()
    page.should_be_correct_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_link()
    add_basket = browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
    add_basket.click()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_link()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    add_basket = browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
    add_basket.click()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_cart()

@pytest.fixture(scope="function")
def setup(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    email = f"user_{time.time()}@fakemail.org"
    password = "StrongPass123!"
    page.register_new_user(email, password)

class TestUserAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_link()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_link()
        add_basket = browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_basket.click()
        page.should_be_correct_name_of_product_in_basket()
        page.should_be_correct_price_in_basket()