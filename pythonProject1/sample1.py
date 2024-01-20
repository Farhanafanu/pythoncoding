class A:
    def sample(self,name):
        self.name=name
        print(self.name)


class B():
    def display(self,mark):
        self.mark=mark
        print(self.mark)


b=B()

b.display(50)
b.sample("farhana")