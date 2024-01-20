class School:
    def student(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        print(self.name,self.roll)

s=School()
s.student("fanu",2)

s.display()