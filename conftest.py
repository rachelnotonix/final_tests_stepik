import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language: en, ru, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nЗапуск браузера с языком: {user_language}")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    print("\nзакрываю драйвер браузера..")
    driver.quit()


@pytest.mark.parametrize("language", "en")
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
