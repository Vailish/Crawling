import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

keyword = input('회사명 : ')

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(f'https://www.teamblind.com/kr/company/{keyword}/reviews')
company = driver.find_element(By.CLASS_NAME, 'name').text


print('#'*100)
print('회사 : ', company)
totalRate = driver.find_element(By.XPATH, '//*[@id="wrap"]/section/div/div/div[2]/div/div/div/div/section[1]/div/div[1]/div[1]/strong').text.split('\n')
print('전체 평점 : ', totalRate)
print('#'*100)
time.sleep(5)  # 사람처럼 보이기위함(차단 방지), 5초간 쉼

reviews = driver.find_elements(By.CLASS_NAME, 'review_item_inr')

for review in reviews:
    score = review.text.split('\n')[1].split(' ')[0]
    comment = review.text.split('\n')[3]
    employee = review.text.split('\n')[5].split(' ')[0]
    id = review.text.split('\n')[5].split(' ')[2]
    position = review.text.split('\n')[5].split(' ')[4]
    reviewDate = review.text.split('\n')[5].split(' ')[-1]
    
    print(id, employee, score, comment)