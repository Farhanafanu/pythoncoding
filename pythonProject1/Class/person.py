
# class Person:
#     def details(self,name,age,job):
#         self.name=name
#         self.age=age
#         self.job=job
#     def display(self):
#         print(self.name,self.age,self.job)
#
#
# p=Person()
# p.details("fanu",25,"Devoloper")
# p.display()
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

p=Person()
p.details("aslam",27)
p.details("farhana",25)