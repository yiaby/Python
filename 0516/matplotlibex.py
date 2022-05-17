"""
matplotlib 라이브러리 활용하여 상품 판매실적 데이터 차트화 시키기
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
#한글 깨짐 방지
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)

#plot() 함수를 활용하여 선 그래프 만들기
plt.plot(["1월","2월","3월"],[120,95,150]) #스마트폰 판매량
plt.plot(["1월","2월","3월"],[50,30,70]) #컴퓨터 판매량
plt.plot(["1월","2월","3월"],[20,15,30]) #OLED TV 판매량

plt.xlabel("월별")
plt.ylabel("판매량")
plt.title("강남 대리점 2022년 상반기 판매실적")
plt.legend(["스마트폰","컴퓨터","OLED TV"])

plt.savefig("./output/matplotSales.svg")