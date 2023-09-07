from pages.book_store_app_page import BookStore_app
from pages.api_account import AccountAPI
from base.demoqa_base import DemoQa
from base.demoqa_api import DemoQaApi
from playwright.sync_api import sync_playwright
from pytest import fixture


def pytest_addoption(parser):
    parser.addoption('--browse', action='store', default='chromium')
    parser.addoption('--headless', action='store', default=True)
    parser.addoption('--browsermode', action='store', default='',  # Browser mode selection
                     help="")


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def get_browser(get_playwright, request):
    browser = request.config.getoption('--browse')
    headless = request.config.getoption('--headless')
    print('browser', browser)
    if browser == 'chromium':
        browser = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        browser = get_playwright.firefox.launch(headless=headless)
    elif browser == 'safari':
        browser = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, "unsupported browser"

    yield browser
    browser.close()


@fixture(scope='function')
def get_app(get_browser):
    return DemoQa(get_browser)


@fixture(scope='function')
def book_store_app(get_browser):
    return BookStore_app(browser=get_browser)

@fixture(scope='function')
def api():
    return DemoQaApi()


@fixture(scope='session')
def account():
    return AccountAPI()