"""
list 자료구조에서 새로운 객체 추가하기
"""
list_name = ['박태호','오수철','손유일','김종오']
list_name.append('이두희')             #append(): list의 맨 마지막에 추가
#print(list_name)                     #['박태호', '오수철', '손유일', '김종오', '이두희']

position = list_name.index('손유일')   #index(): 요소의 인덱스값 출력
print(position)                       #2

#list_name.insert(position,'홍길동')    #insert(): 특정 인덱스 값에 추가
print(list_name)                      #['박태호', '오수철', '홍길동', '손유일', '김종오', '이두희']
"""
#list_name.append(position,'홍길동')  ==> 에러 발생
TypeError: list.append() takes exactly one argument (2 given) ==> append는 인자 값 1개
"""
