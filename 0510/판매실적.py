"""
'L'이라는 전자회사의 2022년 상반기 판매실적을 천단위 마다 콤마 찍는 파이썬 프로그램을 작성하세요.
"""
#자료구조 결정
sales_performance = {"1월":59870000,"2월":37650000,"3월":89425000}

#최적화 소스
items = sales_performance.items()
print("<2022년 상반기 판매실적>")
for key,value in items:
    print(key + "판매 실적: ",format(value,",")+ "원")

# format(항목,"형식지정자")aa




