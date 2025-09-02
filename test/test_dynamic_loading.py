import pytest
import os

from playwright.sync_api import sync_playwright

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

url = 'https://the-internet.herokuapp.com/dynamic_loading/2'
expected = 'Hello World!'

###############################################################
####################  p l a y w r i g h t  ####################
###############################################################

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
    
def test_dynamic_loading(page):
    page.goto(url)
    page.click('#start button') # ID가 start 이라는 객체를 찾아 사용
    
    msg = page.locator('#finish').inner_text().strip()
    # ID가 finish인 객체를 찾아 담겨 있는 텍스트를 추출하고, 앞뒤 공백은 제거
    
    assert expected in msg


###############################################################
######################  s e l e n i u m  ######################
###############################################################

@pytest.fixture(scope='session')
def driver():
    opts = Options()
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        opts.add_argument('--headless=new')
    opts.add_argument('--window-size=1280,900')
    driver = webdriver.Chrome()
    yield driver
    
    driver.quit()
    
def test_dynamic_loading_se(driver):
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, '#start button').click()
    
    fin = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'finish')))
    
    assert expected in fin.text.strip()