import pytest
import os

from web.webpage_login import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    opts = Options()
    # $env:HEADLESS='true'
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        opts.add_argument('--headless=new')
    opts.add_argument('--window-size=1280,900')
    driver = webdriver.Chrome()
    yield driver
    # Test 함수가 driver을 사용하는 동안 잠시 대기
    # return 대용으로 사용
    
    driver.quit()
    # Test 함수 기능 종료 후 드라이버 종료

# autouse=True : 모든 테스트 함수(각 파라미터 케이스 포함) 앞에서 자동으로 세팅    
@pytest.fixture(autouse=True)
def reset_state(driver):
    driver.delete_all_cookies()
    driver.get('about:blank')
    yield
    
LOGIN_CASES = [
    ('tomsmith', 'SuperSecretPassword!', 'You logged into a secure area!')
    , ('tomsmit', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', 'SuperSecretPassword', 'Your password is invalid!')
    , ('', 'SuperSecretPassword!', 'Your username is invalid!')
    , ('tomsmith', '', 'Your password is invalid!')]

@pytest.mark.parametrize('username, pw, expected', LOGIN_CASES)
def test_login_cases(driver, username, pw, expected):
    page = LoginPage(driver)
    page.open()
    page.login(username, pw)
    msg = page.flash_message()
    print(f'Flash msg: {msg}')
    assert expected in msg