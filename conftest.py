import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Which language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        s = Service(ChromeDriverManager().install())
        print("\nstart browser for test..")
        browser = webdriver.Firefox(service=s, options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()

    else:
        options_firefox = OptionsFirefox()
        options_firefox.add_argument("--headless")
        if user_language:
            options_firefox.set_preference("intl.accept_languages", user_language)
        s = Service(GeckoDriverManager().install())
        print("\nstart browser for test..")
        browser = webdriver.Firefox(service=s, options=options_firefox)
        yield browser
        print("\nquit browser..")
        browser.quit()
