import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    print("\nзапускаю браузер для теста..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    print("\nзакрываю драйвер браузера..")
    driver.quit()

@pytest.mark.parametrize('language', "en")
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")