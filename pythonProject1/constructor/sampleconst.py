class Sample:
    def __init__(self,name,age,place):
        self.name=name
        self.place=place
        self.age=age
        print(self.name,self.age,self.place)
    def addage(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
        print(self.place)

s=Sample("aslu",27,"benguluru")
# age=28
# place="mumbai"
s.addage()
s.relocate("mumbai")