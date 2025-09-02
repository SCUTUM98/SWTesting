import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    url = 'https://the-internet.herokuapp.com/login'
    
    # locator setting
    USERNAME = (By.ID, 'username')
    PW = (By.ID, 'password')
    #BTN = (By.CSS_SELECTOR, '[type="submit"]')
    FLASH = (By.ID, 'flash')
    
    def __init__ (self, driver):
        self.driver = driver # 외부 driver를 내부에서 사용하도록 선언
        self.wait = WebDriverWait(driver, 10) # 10초 대기 (웹페이지 지연 대비)
    
    def open(self):
        self.driver.get(self.url)
        print(self.driver.title)
    
    def login(self, username, password):
        
        #wait = WebDriverWait(self.driver, 10)
        id = self.wait.until(ec.visibility_of_element_located(self.USERNAME))
        # 10초간 0.5초 간격으로 특정 기능이 작동 가능할 때 까지 대기
        # "명시적 대기" -> 연결 지연 등과 같은 예상하지 못하는 케이스를 방지하기 위함
        # ec.visibility_of_element_located(locator): 화면에 보일 때 까지
        # ec.element_to_be_clickable(locator): 클릭이 가능할 때 까지
        
        id.clear()
        id.send_keys(username)
            
        pw = self.wait.until(ec.visibility_of_element_located(self.PW))
        pw.clear()
        #pw.send_keys(password)
        pw.send_keys(password, Keys.RETURN)
            
        #btn = ec.element_to_be_clickable(self.BTN)
        #btn.click()
        
    def flash_message(self):
        msg = self.wait.until(ec.visibility_of_element_located(self.FLASH))
        return msg.text.strip()

if __name__ == '__main__':
    opts = Options()
    opts.add_experimental_option('detach', True)
    opts.add_argument('--window-size=1280,900')
    
    driver = webdriver.Chrome(options=opts)
    
    try:
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        page.flash_message()
    finally:
        pass