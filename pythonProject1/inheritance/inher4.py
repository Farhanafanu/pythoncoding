class First:
    def display(self):
        print("first")
class Second:
    def display(self):
        print("second")
class Third(Second):
    def displaythird(self):
        print("third")
s=Third()
s.display()
s.displaythird()
print(Third.mro())
# multilevel inheritance