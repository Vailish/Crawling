from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=vKrBB_3sR8E")
driver.implicitly_wait(3)
print("#"*100)

# title = driver.find_element(by=By.XPATH, value='//*[@id="title"]/h1/yt-formatted-string')
# print(title.text)
print("-"*50)

driver.implicitly_wait(10)

chats = driver.find_elements(by=By.CLASS_NAME, value="style-scope yt-live-chat-item-list-renderer")
for chat in chats:
    time = chat.find_element(by=By.ID, value="timestamp").text
    chatter = chat.find_element(by=By.ID, value="author-name").text
    msg = chat.find_element(by=By.ID, value="message").text
    print(f'{time} {chatter} : {msg}')

print("#"*100)
driver.quit()