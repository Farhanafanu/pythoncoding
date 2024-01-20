class Baseclass:
    def setname(self,name):
        print("hello")
        self.name=name
    def displayname(self):
        print(self.name)
class Subclass(Baseclass):
    def welcome(self):
        print("welcome")
# b=Baseclass()
# b.displayname()
# s=Subclass()
# s.display()
# s.welcome()
s=Subclass()
s.welcome()
s.setname("fanu")
s.displayname()