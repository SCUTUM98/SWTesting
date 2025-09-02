import pytest

from web.plw_login_pw import LoginPage
from playwright.sync_api import sync_playwright

url = "https://the-internet.herokuapp.com/login"
USERNAME = '#username'
PW = '#password'
BTN = 'button[type="submit"]'
MSG = '#flash'

LOGIN_CASES = [
    ('tomsmith', 'SuperSecretPassword!', 'You logged into a secure area!')
    , ('tomsmit', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', 'SuperSecretPassword', 'Your password is invalid!')
    , ('', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', '', 'Your password is invalid!')
    , ('', '', 'Your username is invalid!')]

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    
@pytest.mark.parametrize('username, pw, expected', LOGIN_CASES)
def test_login(page, username, pw, expected):
    page = LoginPage(page)
    page.open()
    page.login(username, pw)
    flash = page.flash_message()
    
    #flash_msg = page.locator(MSG).inner_text().strip()
    assert expected in flash
    