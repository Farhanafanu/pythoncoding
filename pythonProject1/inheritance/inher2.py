class First:
    def display(self):
        print("first")
    # def __init__(self):
    #
    #     print("first class")
class Second:
    def displaysec(self):
        print("second")

    # def __init__(self):
    #     print("second class")
    #
class Third(First,Second):
    def displaythird(self):
        print("third")
t=Third()
t.displaysec()
t.displaythird()
t.display()
# class A:
#     def print(self):
#         print("first A")
# class B:
#     def print(self):
#         print("second B")
# class C(B,A):
#     def print(self):
#         print("third C")
# c=C()
# c.print()