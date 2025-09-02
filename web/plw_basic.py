# pip install playwright
# playwright install
import time

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.naver.com')
        print(page.title())
        time.sleep(2)
        page.screenshot(path='screenshot.png')
        
def mulit_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page1 = browser.new_page()
        page2 = browser.new_page()
        page1.goto('https://www.google.com')
        page2.goto('https://www.naver.com')
        
        print(f'Page 1: {page1.title()}')
        print(f'Page 2: {page2.title()}')
        time.sleep(2)
        page1.screenshot(path='page1_screen.png')
        page2.screenshot(path='page2_screen.png')
        

if __name__ == '__main__':
    run()
    mulit_run()