"""
파이썬으로 빅데이터 파일분석/처리
'연도별 성별 구분하여 출생아 수 통계처리' 하는 프로그램 작성
"""


def countBirths():
    ret = []  # list 자료구조 [{2008, 36253373}], (2009,635342626),
    for y in range(2008, 2019):  # 2008년 ~ 2018년 가지
        count = 0
        filename = 'names/yob%d.txt' % y
        with open(filename, 'r') as f:  # f는 열린 파일 객체
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':  # 한줄의 데이터 마지막 끝이 엔터 '\n' 이면
                    d = d[:-1]  # Emma,F,18813 을 d 변수에 저장

                birth = d.split(',')[2]
                count += int(birth)
        ret.append((y, count))
    return ret


result = countBirths()
with open('birth_by_year.csv', 'w') as f:
    print('년도별 출생아수')
    print('----------------------')
    for year, birth in result:
        data = '%s,%s\n' % (year, birth)
        print(data)
        f.write(data)