import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(xpath, wait_time=30):
    """주어진 XPath에 해당하는 요소를 클릭하는 함수."""
    element = WebDriverWait(browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def select_date(day):
    """주어진 날짜를 선택하는 함수."""
    day_xpath = f'//b[text() = "{day}"]'
    click_element(day_xpath)

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

# '가는 날' 버튼 클릭
click_element('//button[text() = "가는 날"]')

# 27일과 28일 선택
select_date("27")
select_date("28")

# '도착' 버튼 클릭
click_element('//b[text() = "도착"]')

# 뉴욕 선택
click_element('//button[contains(text(), "뉴욕")]')

# 항공권 검색 클릭
click_element('//span[text() = "항공권 검색"]')

# 결과 출력
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="concurrent_ConcurrentItemContainer__NDJda concurrent_with_labels__MWIQQ"]')))
print(elem.text)

input('종료하려면 Enter 키를 입력하세요')
browser.quit()



