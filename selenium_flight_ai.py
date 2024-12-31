import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

# '가는 날' 버튼 클릭
begin_date = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "가는 날"]')))
begin_date.click()

# 27일 선택
day27 = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]')))
day27.click()

# 28일 선택
day28 = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "28"]')))
day28.click()

# '도착' 버튼 클릭
arrival = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//b[text() = "도착"]')))
arrival.click()

# 뉴욕 선택
newyork = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "뉴욕")]')))
newyork.click()

# 항공권 검색 클릭
ticket_search = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[text() = "항공권 검색"]')))
ticket_search.click()

# 결과 출력
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="concurrent_ConcurrentItemContainer__NDJda concurrent_with_labels__MWIQQ"]')))
print(elem.text)

browser.quit()
