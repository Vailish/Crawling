from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://vailish.tistory.com/")
driver.implicitly_wait(0.5)
print("#"*100)

header = driver.find_element(by=By.TAG_NAME, value="header")
value = header.find_element(by=By.CSS_SELECTOR, value="h1 a")
print(value.text)

print("-"*50)

items = driver.find_elements(by=By.CLASS_NAME, value="post-item")
for item in items:
    val = item.find_element(by=By.CLASS_NAME, value="title")
    print(val.text)

print("#"*100)
driver.quit()

# driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title = driver.title

# driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

# driver.quit()