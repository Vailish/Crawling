import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import parse

# keyword = input('회사명 : ')

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(f'http://www.yes24.com/Product/Goods/117651459')


print('#'*100)

book_name = driver.find_element(By.CLASS_NAME, 'gd_name').text
print('도서명 : ', book_name)

book_rate = driver.find_element(By.CLASS_NAME, 'yes_b').text
print('전체 평점 : ', book_rate)

book_isbm = driver.find_element(By.XPATH, '//*[@id="infoset_specific"]/div[2]/div/table/tbody/tr[3]/td').text
print('ISBM13 : ', book_isbm)

book_rate_ages = driver.find_elements(By.XPATH, '//*[@id="ageChart"]/ul')

book_detail = driver.find_element(By.XPATH, '//*[@id="infoset_inBook"]/div[2]/div[1]/div[1]').text
print(book_detail)

for book_rate_age in book_rate_ages:
    print(book_rate_age.text.split('\n'))

print('#'*100)

reviews = driver.find_elements(By.CLASS_NAME, 'reviewInfoGrp.lnkExtend')
for review in reviews:
    # 아이디
    try:
        if "YES마니아" in review.text.split('|')[1].strip():
            print(review.text.split('|')[1].strip().split(" ")[-1])
        else:
            print(review.text.split('|')[1].strip())
    except:
        pass

    # 타이틀
    print(review.text.split('\n')[0])

    # 내용
    print(review.text.split('l\n'))


time.sleep(2)