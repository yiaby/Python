"""
파이썬의 전역변수와 지역변수 실습 예제
"""
param = 10
strdata = '전역변수'

def func1():
   strdata = '지역 변수'
   print(strdata)

def func2(param):
    param = 1

def func3():
    global param #global : 전역변수 예약어  
    param = 50

func1() #func1함수 호출 =>'지역 변수' 출력
print(strdata) #=>'전역변수' 출력

func2(param)
print(param) #=>전역변수 10출력 

func3()
print(param) #=>전역변수가 10에서 50으로 바뀜

#멤버 체크하기
listdata = [10, 20, 30, 40]
result1 = 50 in listdata  #값 in 자료구조

print(result1) #False

result2 = 40 in listdata

print(result2) #True 


