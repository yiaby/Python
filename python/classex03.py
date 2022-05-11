class Add:
    def add(self,n1,n2):
         return n1+n2

class Calculator(Add):      #class 자식클래스명(부모클래스이름):         <-상속
    def sub(self,n1,n2):
        return n1-n2

obj = Calculator()
print(obj.add(10,20))
print(obj.sub(30,10))
    
    
   
    
