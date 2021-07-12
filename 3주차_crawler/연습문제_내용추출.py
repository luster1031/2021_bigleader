#4번

#Step 1. 필요한 모듈을 로딩합니다
from selenium import webdriver
import time          

#Step 2. 사용자에게 검색 관련 정보들을 입력 받습니다.
query_txt = input('1.수집할 자료의 키워드는 무엇입니까?(여러개일 경우 , 로 구분하여 입력): ')
print("\n")

#Step 3. 크롬 드라이버 설정 및 웹 페이지 열기
chrome_path = "C:/tmp/chromedriver_85/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = 'https://korean.visitkorea.or.kr/main/main.do#home'
driver.get(url)
time.sleep(2)

#Step 4. 자동으로 검색어 입력 후 조회하기
element = driver.find_element_by_xpath('//*[@id="inp_search"]')
#element = driver.find_element_by_id("query")
driver.find_element_by_xpath('//*[@id="inp_search"]').click( )
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(2)


#Step 6.Beautiful Soup 로 본문 내용만 추출하기
from bs4 import BeautifulSoup
html_1 = driver.page_source #현재 페이지의 전체 소스코드를 다 가져오기
soup_1 = BeautifulSoup(html_1, 'html.parser')


# find ('태그명','속성 값')
# find ('div', 'title') = find('div', class_ = "title")

content_1 = soup_1.find('div','area_sWordList').find_all('li')
for i in content_1 :
    txt = i.find('em').get_text()
    print(txt)
    print("\n")
    #print(i.get_text().replace("\n"," ").strip())
    #print("\n")
    
driver.maximize_window()
