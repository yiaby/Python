"""
네이버 날씨 웹 크롤링 하기
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

url ='https://weather.naver.com/today/09140104'

f = urlopen(url)
fp = f.read()
f.close()

soup = BeautifulSoup(fp,'html.parser')

location = soup.select_one('.location_name').get_text().strip()
temperature = soup.select_one('.current').get_text().strip()
temperature_up = soup.select_one('.summary').get_text().strip()


print(location,temperature,temperature_up)
