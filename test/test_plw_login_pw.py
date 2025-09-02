import pytest

from playwright.sync_api import sync_playwright

url = "https://the-internet.herokuapp.com/login"
LOGIN_CASES = [
    ('tomsmith', 'SuperSecretPassword!', 'You logged into a secure area!')
    , ('tomsmit', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', 'SuperSecretPassword', 'Your password is invalid!')
    , ('', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', '', 'Your password is invalid!')]

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
    page.goto(url)
    
    page.fill('#username', username)
    page.fill('#password', pw)
    page.click('button[type="submit"]')
    
    flash_msg = page.locator('#flash').inner_text().strip()
    assert expected in flash_msg
    