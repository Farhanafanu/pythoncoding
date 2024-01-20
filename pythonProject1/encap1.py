class Student:
    def __init__(self,name,age):
        self._name=name
        self.__age=age
    def display(self):
        print({self._name},{self.__age})
    def update(self,newage):
        if newage>0:
            self.__age=newage
            print("age updated")
        else:
            print("invalid")
s=Student("aju",23)
s.display()
s.update(27)
s.display()