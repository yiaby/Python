class MyClass:
    var = '안녕하세요' #클래스 멤버

    def sayHello(self): #클래스 메소드 
       print(self.var)

obj = MyClass() #인스턴스 객체

print(obj.var)
obj.sayHello()

        
