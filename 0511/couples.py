from random import shuffle
from time import sleep

male = ['김진홍','윤종인','홍지수','이형준','유동희']
female = ['성지영','김은정','김선정','이현아','이은진']

shuffle(male)
shuffle(female)

couples = zip(male,female)
couples_data = list(couples)

for i,couple in enumerate (couples_data):
    print("커플[%d]: [%s]♥[%s]"%(i+1,couple[0],couple[1]))

