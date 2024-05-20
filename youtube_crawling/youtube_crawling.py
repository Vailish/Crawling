from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver 경로 설정
CHROME_DRIVER_PATH = 'path/to/chromedriver'  # 여기에 실제 chromedriver 경로를 입력하세요.

# YouTube 라이브 URL 설정
url = 'https://www.youtube.com/watch?v=Mm2qIQCI9Yk'

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# WebDriver 서비스 설정
# service = Service(CHROME_DRIVER_PATH)
service = Service("C:/Users/joyks/Desktop/crawling/chrome-win64/chrome-win64")
driver = webdriver.Chrome(service=service, options=chrome_options)

# YouTube 페이지 열기
driver.get(url)

print("#" * 100)

# 페이지 로드 대기
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents")))

# 채팅 메시지 요소 찾기
chat_items = driver.find_elements(By.CSS_SELECTOR, "#items .yt-live-chat-text-message-renderer")

# 각 채팅 메시지 출력
for item in chat_items:
    author = item.find_element(By.CSS_SELECTOR, '#author-name').text
    message = item.find_element(By.CSS_SELECTOR, '#message').text
    timestamp = item.find_element(By.CSS_SELECTOR, '#timestamp').text
    print(f"[{timestamp}] {author}: {message}")

print("#" * 100)

# 드라이버 종료
driver.quit()



# book_rate = driver.find_element(By.CLASS_NAME, 'yes_b').text
# print('전체 평점 : ', book_rate)

# book_rate_ages = driver.find_elements(By.XPATH, '//*[@id="ageChart"]/ul')
# for book_rate_age in book_rate_ages:
#     print(book_rate_age.text.split('\n'))

# id="chat-container"
# id="contents"

# id="content"
# id="timestamp"
# id="author-name"
# id="message"