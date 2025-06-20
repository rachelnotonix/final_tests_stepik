from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.XPATH, "//a[@id='registration_link']")


class LoginPageLocators:

    LOGIN_PAGE = (By.XPATH, "//title[contains(text(), 'Login or register')]")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators:
    # локатор для кнопки добавления в корзину
    ADD_BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    # локатор для сообщения, что товар добавлен на страницу
    MESSAGE_ADDED_ITEM = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    # локатор для стоимости корзины
    VALUE_OF_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    # локатор, что книга добавлена в корзину успешно
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'has been added to your basket')]",
    )


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_PAGE = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
