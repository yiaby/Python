"""
게임 횟수를 입력받아 로또번호 자동 발생기를
파이썬 프로그램으로 작성
"""
from random import shuffle
from time import sleep

gamenum =int(input("로또 게임 회수를 입력하세요>>>"))

listdata = list(range(1,46))

for i in range(1,gamenum+1):
    shuffle(listdata)
    print("로또번호[%d]:"%i,sorted(listdata[:6])) #sorted :원본은그대로두고 정렬한 리스트를 반환
    sleep(1) # 1sec 쓰로들링이 일어날 수 있기 때문에 조절해야함