"""
 파이썬으로 자동판매기 프로그램 작성
"""
money = int(input("투입된 돈: ")) #콘솔창에서 입력받은 값을 정수값으로 변환 (정수로 입력해도 문자열로 인식됨)             
price = int(input("상품값: "))

change = money - price
print("거스름 돈 : ", change)

coin500 = change // 500
coin100 = (change-coin500*500)//100
print("500원 : " , coin500, "개")
print("100 원 : " , coin100, "개")
  
