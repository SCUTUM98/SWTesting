# 모의 객체 (Mock) 기본
# - 외부 API를 호출하지 않고, 가짜 함수(Mock)을 주입해서 검증
########################  E x a m p l e  ########################
# def test_convert_usd_to_krw():
#     # 1. 가짜(Mock) 함수 생성
#     fake_get_rate = mock(return_value=1300)
#     # 2. convert_usd_to_krw() 에 가짜 데이터 주입
#     result = convert_usd_to_krw(10, get_rate_func=fake_get_rate)
#     # 3. 검증
#     assert result == 13000

from playwright.sync_api import sync_playwright, Page

URL = "file:///Users/bongeungu/Desktop/swtest/SWTesting/web/signup.html"

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # 요소 locator
        self.email = page.locator("#email")
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.confirm = page.locator("#confirm")
        self.terms = page.locator("#terms")
        self.submit_btn = page.locator("button[type=submit]")
        self.flash = page.locator("#flash")

    def open(self, url=URL):
        self.page.goto(url)

    def fill_form(self, email, username, password, confirm, terms=True):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)
        self.confirm.fill(confirm)
        if terms:
            self.terms.check()
        else:
            self.terms.uncheck()

    def submit(self):
        self.submit_btn.click()

    def flash_message(self) -> str:
        self.flash.wait_for(state='visible')
        # 화면 전환이 flash msg 출력보다 빨라 msg를 인식하는 문제 발생
        # 해결을 위해 flash msg가 확실하게 출력되는걸 확인한 후에 msg를 읽어오도록 변경
        return self.flash.inner_text().strip()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        signup = SignupPage(page)
        signup.open()
        signup.fill_form(
            email="user@example.com",
            username="tester",
            password="abc12345",
            confirm="abc12345",
            terms=True,
        )
        signup.submit()
        print("Flash message:", signup.flash_message())

        browser.close()