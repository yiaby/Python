weight = float(input("몸무게를 kg 단위로 입력하세요>>>"))
height = float(input("키를 m 단위로 입력하세요>>>"))

bmi = (weight/(height**2))

if 20 <= bmi and bmi <= 25:
    decision = "정상"
elif 25.1 <= bmi and bmi <= 29.9:
    decision = "과체중"
elif 30 <= bmi and bmi <= 40:
    decision = "비만"
elif bmi >= 40:
    decision = "고도비만"

print("BMI지수는",bmi,"이며,",decision,"입니다.")