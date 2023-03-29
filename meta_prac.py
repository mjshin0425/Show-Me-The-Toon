import requests                                  # requests:웹에 접속하는 라이브러리
from bs4 import BeautifulSoup                    # BeautifulSoup : 데이터를 솎아내는 라이브러리

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://comic.naver.com/webtoon')

soup = BeautifulSoup(data.text, 'html.parser')    # 코딩시작

a = soup.select_one('#container > div.component_wrap.type2 > div.WeekdayMainView__daily_all_wrap--UvRFc')

a = 1
b = 2
print(a+b)


# image = soup.select_one('meta[class="Poster__image--d9XTI"]')
# title = soup.select_one('meta[class="ContentTitle__title--e3qXt"]')
# review = soup.select_one('meta[class="Poster__link--sopnC"]')
# print(image,title)

# Poster__link--sopnC
