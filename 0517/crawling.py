"""
  벅스 차트 사이트 접속하여 성인가요 1 ~ 10순위 까지 데이터 웹 크롤링 하기
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

url ='https://music.bugs.co.kr/genre/chart/kpop/adultkpop/total/day'

f = urlopen(url)
fp = f.read()
f.close()

soup = BeautifulSoup(fp,'html.parser')

titles = soup.select('p.title')
artists = soup.select('p.artist')

print("금일 가요 TOP 10 >>>")
for i in range(0,10):
    title = titles[i].text.strip()
    artist = artists[i].text.strip()
    print(i+1,title,'-',artist)

