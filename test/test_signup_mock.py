import pytest
import json
import time

from playwright.sync_api import sync_playwright
from web.sign_up import SignupPage

URL = "file:///Users/bongeungu/Desktop/swtest/SWTesting/web/signup_mock.html"

CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status": "ok", "message": "회원가입 성공(Mocked)"},
        "expected": "회원가입 성공(Mocked)",
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status": "error", "message": "서버 오류(Mocked)"},
        "expected": "서버 오류(Mocked)",
    },
]
# 서버에 접속했다고 가정하는 케이스

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
    
@pytest.mark.parametrize('case', CASES)
# 딕셔너리 타입의 케이스 전달시, 하나로 묶어서 전달 가능
def test_signup_mock(case, page):
    def fake_signup_api(route, request):
        route.fulfill(
            status = case['status'],
            content_type = 'application/json',
            body = json.dumps(case['json_body'])
        )
    
    page.route('**/api/signup', fake_signup_api)
    
    signup = SignupPage(page)
    signup.open(URL)
    signup.fill_form('user@ex.com', 'tester', '12345678', '12345678', True,) # 테스트 케이스 자동 입력
    signup.submit()
    flash = signup.flash_message()
    assert case['expected'] in flash