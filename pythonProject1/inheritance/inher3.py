class First:
    def display(self):
        print("first")
class Second:
    def display(self):
        print("second")
class Third(First,Second):
    def displaythird(self):
        print("third")
s=Third()
s.displaythird()
s.display()
