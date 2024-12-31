import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

#time.sleep(1) # 1초 대기
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]')))
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "28"]')))
day3 = browser.find_elements(By.XPATH, '//b[text() = "28"]')
day3[1].click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "도착"]')))
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "뉴욕")]')))
newyork = browser.find_element(By.XPATH, '//button[contains(text(), "뉴욕")]')
newyork.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//span[text() = "항공권 검색"]')))
ticket_search = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
ticket_search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="concurrent_ConcurrentItemContainer__NDJda concurrent_with_labels__MWIQQ"]')))
print(elem.text)

browser.quit()