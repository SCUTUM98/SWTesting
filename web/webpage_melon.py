import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_experimental_option('detach', True)
opts.add_argument('--window-size=1280,900') # 브라우저 사이즈 고정

driver = webdriver.Chrome(options=opts)

try:
    driver.get('https://www.melon.com')
    print(driver.title)
    
    el = driver.find_element(By.ID, 'top_search')
    el.clear()
    el.send_keys('BTS', Keys.RETURN)
    
    driver.find_element(By.CSS_SELECTOR, '[title="앨범 - 페이지 이동"]').click()
    #driver.find_element(By.CSS_SELECTOR, '[title="LOVE YOURSELF 結 \'Answer\' - 페이지 이동"]').click()
    driver.find_element(By.CSS_SELECTOR, '#frm > div > ul > li:nth-child(1) > div > div > dl > dt > a').click()
    # copy > selector copy
    driver.find_element(By.CSS_SELECTOR, '[title="Euphoria 곡정보"]').click()
    
    lyrics = driver.find_element(By.ID, 'd_video_summary').text
    title = driver.find_element(By.CLASS_NAME, 'song_name').text
    print(f'========== {title} ==========')
    print(lyrics)
    
    file_object = open("web/lyrics.txt", "w+")
    file_object.write(f'========== {title} ==========\n')
    file_object.write(lyrics)
    file_object.close()
    
    with open(f'web/{title}_lyrics.txt', 'w', encoding='utf-8') as file:
        file.write(f'========== {title} ==========\n')
        file.write(lyrics)
    print(f'{title}_lyrics.txt has saved')
    
finally:
    pass
