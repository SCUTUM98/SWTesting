import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome driver 강제 종료 방지
opts = Options()
opts.add_experimental_option('detach', True)
#opts.add_argument('--headless=new') # Background 브라우저 작업용
opts.add_argument('--window-size=1280,900') # 브라우저 사이즈 고정

driver = webdriver.Chrome(options=opts)

#driver = webdriver.Chrome()
try:
    driver.get('https://www.python.org')
    print(driver.title)
    
    el = driver.find_element(By.NAME, 'q')
    el.clear()
    el.send_keys('pycon', Keys.RETURN)
finally:
    pass
    #driver.quit()