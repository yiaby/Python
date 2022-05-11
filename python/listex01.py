"""
 리스트(list)자료구조 실습 예제
"""
list1 = [10,20,30,40,50]
list2 = ['a', 'b', 'c']
list3 = [10, 'a', 'abc', [10,20,30,40,50], ['a','b','c']]
list1[0] = 60 #list는 데이터 변경이 가능하다. 

print(list1)

def myfunc():
    print('Python Good!')

list4 = [10, 20, myfunc]
list4[2]() #myfunc함수를 호출 

"""
 튜플(tuple)자료구조 실습 예제
"""
tuple1 = (10,20,30,40,50)
tuple2 = ('a', 'b', 'c')
tuple3 = (10, 'a', 'abc', [10,20,30,40,50], ['a','b','c'])
#tuple1[0] = 60 -->에러발생:tuple은 데이터변경을 할 수 없다.

print(tuple1)

def myfunc():
    print('Python Good!')

tuple4 = (10, 20, myfunc)
tuple4[2]() #myfunc함수를 호출 

    
