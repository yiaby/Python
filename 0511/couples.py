from random import shuffle
from time import sleep

male = ['김진홍','윤종인','홍지수','이형준','유동희']
female = ['성지영','김은정','김선정','이현아','이은진']

shuffle(male)
shuffle(female)
#zip()함수는 각 리스트의 동일한 인덱스의 요소 끼리 묶는다.
#zip()함수의 결과를 list로 형변환 하지 않으면 출력할때 에러가 발생할 수 있다.
couples = zip(male,female)
couples_data = list(couples)

for i,couple in enumerate (couples_data):
    print("커플[%d]: [%s]♥[%s]"%(i+1,couple[0],couple[1]))

