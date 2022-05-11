class Member:
    #속성 생성(객체의 초기화 개념)
    #클래스 생성자는 Member 클래스의 인스턴스 객체가 생성될 때 자동적으로 호출된다 
    def __init__(self, name, age, address):      
     self.name=name
     self.age = age
     self.address = address

     #메소드 생성
    def info(self):
            print('회원의 이름은{0}이고, 나이는{1}, 주소는{2}입니다.'.format(self.name,self.age,self.address))

introduce = Member('홍길동',28,'서울 논현동')
introduce.info()
         
