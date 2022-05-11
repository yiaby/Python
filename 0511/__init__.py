"""
게임 횟수를 입력받아 로또번호 자동 발생기를
파이썬 프로그램으로 작성
"""
from random import shuffle
from time import sleep

gamemnum =input("로또 게임 회수를 입력하세요>>>")

for i in range(int(gamemnum)):
    balls = list(range(1,46))   #1~45까지 만들겠다.
    lottoresult = []            #데이터가 없는 빈 리스트 자료구조 생성

    for j in range(6):          #0~5 즉 6번 반복해라
        shuffle(balls)          #1~45까지를 무작위로 썩는다.
        number = balls.pop()
        lottoresult.append(number)
    lottoresult.sort()                  #오름차순 정렬시켜라
    print("로또번호[%d]:"%(i+1),end="")
    print(lottoresult)
    sleep(1)