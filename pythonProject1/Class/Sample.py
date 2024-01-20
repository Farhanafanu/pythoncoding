class Sample:
    def hello(self,n):
        self.name=n
        #
    def nameprint(self):
        print(self.name)
s=Sample()
y=Sample()

 # name="fanu"
# s.hello(name)
# s.hello("aslu")
name="Aslu"
s.hello(name)
s.nameprint()
s.hello("fanu")
s.nameprint()


