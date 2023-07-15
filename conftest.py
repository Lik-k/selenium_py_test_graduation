from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# def browser(request):
#     browser = webdriver.Chrome
#     print("\nstart browser")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
