class Sample:
    def setname(self,name):
        self.name=name
        print(self.name)
    def __add__(self, other):
        fullname=self.name+" "+other.name
        return fullname


firstname=Sample()
secondname=Sample()
firstname.setname("aslu")
secondname.setname("fanu")
fullname=firstname+secondname
print(fullname)

