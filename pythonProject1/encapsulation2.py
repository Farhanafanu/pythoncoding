
class Student:
    def exam(self,name,mark):
        self._name=name
        self.__mark=mark
    def display(self):
        print(self._name,self.__mark)

    def update(self,newmark):
        if newmark>0:
            self.__mark=newmark
        else:
            print("invalid")

s=Student()
s.exam("anu",10)
s.display()
s.update(50)
s.display()