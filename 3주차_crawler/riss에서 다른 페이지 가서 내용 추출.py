#Step 5.학위 논문 선택하기
# 눌렀을 때, 다른 페이지 가는거 
driver.find_element_by_link_text('학위논문').click()
time.sleep(2)

#Step 6.Beautiful Soup 로 본문 내용만 추출하기
from bs4 import BeautifulSoup
html_1 = driver.page_source #현재 페이지의 전체 소스코드를 다 가져오기
soup_1 = BeautifulSoup(html_1, 'html.parser')


# find ('태그명','속성 값')
# find ('div', 'title') = find('div', class_ = "title")
content_1 = soup_1.find('div','srchResultListW').find_all('li')
for i in content_1 :
    print(i.get_text().replace("\n"," ").strip())
    print("\n")
