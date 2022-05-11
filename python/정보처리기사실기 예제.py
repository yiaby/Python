#정보처리 실기문제 풀이(1)
country = {"한국","일본","미국","프랑스"}
country.add("영국")
country.add("싱가폴")
country.remove("일본")
country.update(["홍콩","한국","스위스"])
print(country)
#[정답]=>한국,미국,프랑스,영국,싱가폴,홍콩,스위스 (실행할때마다 순서바뀜)

#정보처리 실기문제 풀이(2)
class good:
    li = ['seoul','kyoengy','inchon','daejeon','daegu','pusan']
g = good() #good인스턴스 객체 생성
str01 = ''


for i in g.li:
     str01 = str01 + i[0]
print(str01)

   # 정답: skiddp
   
#정보처리 실기문제 풀이(3)
lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0]) #[1,2,3]
print(lol[2][1]) #7
                   
for sub in lol:
    for item in sub:
        print(item, end='') #123 45 6789
    print()#줄바꿈   

#[정답]

#정보처리 실기문제 풀이(4)
li=['Korea','America','China']
a=0
str01=''

for i in li:
     for j in i:
       str01 += j[0]
       a=a+1
       if a>5:
           break
          
print('a: ',a,'str01: ',str01)
        
#[결과 ]a:  ,str01:

#정보처리 실기 기출문데5 풀이
a,b = 100,200
print(a==b)
#정답 False =>첫자는 대문자로함.

#정보처리 실기 기출문제6 풀이
a=100
result=0

for i in range(1,3): #1부터 3미만 까지 => 즉 1,2
    result = a>>i #>>비트(0 또는 1) 연산자
    result = result +1
print(result)
#정답 : 26 
# 64 32 16 8 4 2 1
#  1   1   0 0 1 0 0
#  0   1   1 0 0 1 0 0    =>50+1=51
#  0   1   1 0 0 1 1
#  0   0   1 1 0 0 1 1    =>25+1=26

strdata = 'Time is money!!' #음수는 뒤부터 -1로 시작함.
listdata = [1,2,[1,2,3]]

print(strdata[5])
print(strdata[-2])
print(listdata[0])
print(listdata[-1])
print(listdata[2][-1])

#문자열 자료 슬라이싱=>[시갖인덱스:끝인덱스:스텝]
#시직인엑스 이상부터 끝인데긋 미만까지
print(strdata[1:5]) #[정답]'ime '(공백도 문자열로 포함 함)
print(strdata[:7])  #'[정답]Time is'(공백도 무자열로 포함 함)
print(strdata[9:])  #'oney!!'
print(strdata[:-3]) #'Time is mone'
print(strdata[-3:]) #'y!!'
print(strdata[:])    #'Time is money!!'
print(strdata[: :2]) #'Tm smmy!'



















